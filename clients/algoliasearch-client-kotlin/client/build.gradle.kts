import org.jetbrains.kotlin.gradle.ExperimentalKotlinGradlePluginApi
import org.jetbrains.kotlin.konan.target.HostManager

plugins {
  kotlin("multiplatform")
  kotlin("plugin.serialization")
  id("com.vanniktech.maven.publish")
  id("com.diffplug.spotless")
  id("binary-compatibility-validator")
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
      languageSettings {
        optIn("kotlinx.coroutines.ExperimentalCoroutinesApi")
        optIn("kotlinx.serialization.ExperimentalSerializationApi")
        optIn("com.algolia.client.InternalAlgoliaClient")
      }
    }
    val commonMain by getting {
      dependencies {
        api(libs.ktor.client.core)
        api(libs.kotlinx.serialization.json)
        api(libs.ktor.client.logging)
        implementation(libs.ktor.client.serialization.json)
        implementation(libs.ktor.client.content.negotiation)
        implementation(libs.kotlin.datetime)
      }
    }
  }
}
