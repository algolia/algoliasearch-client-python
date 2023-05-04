rootProject.name = "kotlin-playground"

includeBuild("../../clients/algoliasearch-client-kotlin") {
    dependencySubstitution {
        substitute(module("com.algolia:algoliasearch-client-kotlin")).using(project(":client"))
    }
}
