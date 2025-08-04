//
//  {{cookiecutter.app_name}}App.swift
//  {{cookiecutter.app_name}}
//
//  Created by {{cookiecutter.author_name}} on {% now 'utc', '%d/%m/%y' %}.
//

import SwiftUI
{% if cookiecutter.use_swift_data == "true" %}import SwiftData{% endif %}

@main
struct {{cookiecutter.app_name}}App: App {
    {% if cookiecutter.use_swift_data == "true" %}
    let container: ModelContainer
    
    init() {
        do {
            container = try ModelContainer(for: Item.self)
        } catch {
            fatalError("Could not initialize ModelContainer")
        }
    }
    {% endif %}
    
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        {% if cookiecutter.use_swift_data == "true" %}
        .modelContainer(container)
        {% endif %}
    }
} 