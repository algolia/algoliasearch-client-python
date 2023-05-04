import com.diffplug.gradle.spotless.SpotlessExtension
import org.gradle.api.tasks.testing.logging.TestExceptionFormat
import org.gradle.api.tasks.testing.logging.TestLogEvent.*
import org.jetbrains.kotlin.gradle.ExperimentalKotlinGradlePluginApi
import org.jetbrains.kotlin.konan.target.HostManager

@Suppress("DSL_SCOPE_VIOLATION")
plugins {
    alias(libs.plugins.kotlin.multiplaform)
    alias(libs.plugins.kotlinx.serialization)
    alias(libs.plugins.spotless)
}

repositories {
    mavenCentral()
}


@OptIn(ExperimentalKotlinGradlePluginApi::class)
kotlin {
    targetHierarchy.default()

    explicitApi()
    jvm()

    if (HostManager.hostIsMac) {
        iosX64()
        iosArm64()
        iosSimulatorArm64()
    }

    sourceSets {
        all {
            languageSettings.apply {
                optIn("kotlinx.coroutines.ExperimentalCoroutinesApi")
                optIn("kotlinx.serialization.ExperimentalSerializationApi")
            }
        }

        val commonTest by getting {
            dependencies {
                implementation("com.algolia:algoliasearch-client-kotlin")
                implementation(kotlin("test-common"))
                implementation(kotlin("test-annotations-common"))
                implementation(libs.coroutines.test)
                implementation(libs.kotlinx.serialization.json)
            }
        }

        val jvmTest by getting {
            dependencies {
                implementation(kotlin("test-junit"))
                implementation(libs.ktor.client.okhttp)
            }
        }

        if (HostManager.hostIsMac) {
            val appleTest by getting {
                dependencies {
                    implementation(libs.ktor.client.darwin)
                }
            }
        }
    }
}

tasks.withType<Test> {
    testLogging {
        events(STARTED, PASSED, SKIPPED, FAILED)
        exceptionFormat = TestExceptionFormat.FULL
        showStandardStreams = false
    }
}

configure<SpotlessExtension> {
    kotlin {
        target("**/*.kt")
        trimTrailingWhitespace()
        ktlint()
            .editorConfigOverride(
                mapOf(
                    "ktlint_standard_no-wildcard-imports" to "disabled",
                    "ktlint_standard_trailing-comma-on-declaration-site" to "disabled",
                ),
            )
    }
}
