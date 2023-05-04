import com.diffplug.gradle.spotless.SpotlessExtension

@Suppress("DSL_SCOPE_VIOLATION")
plugins {
  alias(libs.plugins.kotlin.multiplaform) apply false
  alias(libs.plugins.kotlinx.serialization) apply false
  alias(libs.plugins.kotlinx.binary.validator) apply false
  alias(libs.plugins.maven.publish) apply false
  alias(libs.plugins.spotless) apply false
}

subprojects {
  apply(plugin = "com.diffplug.spotless")
  configure<SpotlessExtension> {
    kotlin {
      target("**/*.kt")
      ktlint()
        .editorConfigOverride(
          mapOf(
            "ktlint_standard_no-wildcard-imports" to "disabled",
            "ktlint_standard_trailing-comma-on-declaration-site" to "disabled",
          ),
        )
    }
  }
}

tasks.register<Delete>("clean") {
  delete(rootProject.buildDir)
}
