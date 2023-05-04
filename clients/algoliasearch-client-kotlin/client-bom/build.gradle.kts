plugins {
  id("com.vanniktech.maven.publish")
  id("java-platform")
}

dependencies {
  constraints {
    api(projects.client)
    api(libs.ktor.client.android)
    api(libs.ktor.client.apache)
    api(libs.ktor.client.cio)
    api(libs.ktor.client.java)
    api(libs.ktor.client.jetty)
    api(libs.ktor.client.okhttp)
  }
}
