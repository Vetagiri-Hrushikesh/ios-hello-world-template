//
//  ContentView.swift
//  {{cookiecutter.app_name}}
//
//  Created by {{cookiecutter.author_name}} on {% now 'utc', '%d/%m/%y' %}.
//

import SwiftUI
{% if cookiecutter.use_swift_data == "true" %}import SwiftData{% endif %}

struct ContentView: View {
    {% if cookiecutter.use_swift_data == "true" %}
    @Environment(\.modelContext) private var modelContext
    @Query private var items: [Item]
    {% endif %}
    
    var body: some View {
        VStack(spacing: 20) {
            Image(systemName: "globe")
                .imageScale(.large)
                .foregroundStyle(.tint)
                .font(.system(size: 60))
            
            Text("Hello, World!")
                .font(.largeTitle)
                .fontWeight(.bold)
            
            Text("Welcome to {{cookiecutter.app_name}}")
                .font(.title2)
                .foregroundColor(.secondary)
            
            Text("Version {{cookiecutter.version_name}}")
                .font(.caption)
                .foregroundColor(.secondary.opacity(0.7))
        }
        .padding()
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .background(Color(.systemBackground))
    }
}

#Preview {
    ContentView()
    {% if cookiecutter.use_swift_data == "true" %}
    .modelContainer(for: Item.self, inMemory: true)
    {% endif %}
}
