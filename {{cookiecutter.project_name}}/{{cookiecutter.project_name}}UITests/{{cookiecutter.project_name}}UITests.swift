//
//  {{cookiecutter.app_name}}UITests.swift
//  {{cookiecutter.app_name}}UITests
//
//  Created by {{cookiecutter.author_name}} on {% now 'utc', '%d/%m/%y' %}.
//

import XCTest

final class {{cookiecutter.app_name}}UITests: XCTestCase {

    override func setUpWithError() throws {
        // Put setup code here. This method is called before the invocation of each test method in the class.

        // In UI tests it is usually best to stop immediately when a failure occurs.
        continueAfterFailure = false

        // In UI tests it's important to set the initial state - such as interface orientation - required for your tests before they run. The setUp method is a good place to do this.
    }

    override func tearDownWithError() throws {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
    }

    @MainActor
    func testExample() throws {
        // UI tests must launch the application that they test.
        let app = XCUIApplication()
        app.launch()

        // Use XCTAssert and related functions to verify your tests produce the correct results.
        XCTAssertTrue(app.staticTexts["Hello, World!"].exists)
        XCTAssertTrue(app.staticTexts["Welcome to {{cookiecutter.app_name}}"].exists)
    }

    @MainActor
    func testLaunchPerformance() throws {
        // This measures how long it takes to launch your application.
        measure(metrics: [XCTApplicationLaunchMetric()]) {
            XCUIApplication().launch()
        }
    }
} 