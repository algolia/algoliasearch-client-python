plugins {
    kotlin("jvm") version "1.8.22"
    kotlin("plugin.serialization") version "1.8.22"
}

group = "com.algolia"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    implementation("com.algolia:algoliasearch-client-kotlin")
    implementation("io.ktor:ktor-client-okhttp:2.3.1")
    implementation("ch.qos.logback:logback-classic:1.4.8")
    implementation("io.github.cdimascio:dotenv-kotlin:6.4.1")
}

tasks.test {
    useJUnitPlatform()
}

kotlin {
    jvmToolchain(11)
}
