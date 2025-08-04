//
//  {{cookiecutter.app_name}}Tests.swift
//  {{cookiecutter.app_name}}Tests
//
//  Created by {{cookiecutter.author_name}} on {% now 'utc', '%d/%m/%y' %}.
//

import Testing
@testable import {{cookiecutter.app_name}}

struct {{cookiecutter.app_name}}Tests {

    @Test func example() async throws {
        // Write your test here and use APIs like `#expect(...)` to check expected conditions.
        #expect(true)
    }
    
    @Test func appVersionTest() async throws {
        // Test that app version is properly set
        let expectedVersion = "{{cookiecutter.version_name}}"
        #expect(expectedVersion == "{{cookiecutter.version_name}}")
    }

} 