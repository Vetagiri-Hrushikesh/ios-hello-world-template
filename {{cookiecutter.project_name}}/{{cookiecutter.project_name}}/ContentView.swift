//
//  ContentView.swift
//  {{cookiecutter.project_name}}
//
//  Created by {{cookiecutter.author_name}} on {% now 'utc', '%d/%m/%y' %}.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            Image(systemName: "globe")
                .imageScale(.large)
                .foregroundStyle(.tint)
            Text("Hello, iOS!")
                .font(.title)
                .fontWeight(.bold)
            Text("Welcome to {{cookiecutter.project_name}}")
                .font(.subheadline)
                .foregroundColor(.secondary)
        }
        .padding()
    }
}

#Preview {
    ContentView()
}
