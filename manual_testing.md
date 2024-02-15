[Return to the README](README.md)


| Testcase                          | Expected Result                                                       | Test Result |
|-----------------------------------|-----------------------------------------------------------------------|-------------|
| Logo is clicked             | Home page is loaded successfully                     | ✅ PASS          |
| Search for existing object             | Object is loaded successfully                     | ✅ PASS          |
| Search for non-existing object             | Nothing is loaded                      | ✅ PASS          |
| Open the Homepage                 | Home page is loaded successfully                     | ✅ PASS          |
| Open the Perfumes Page                | Perfumes page is loaded successfully                     | ✅ PASS          |
| Open the Sign Up Page                | Sign Up page is loaded successfully                     | ✅ PASS          |
| Open the Login Page                | Login page is loaded successfully                     | ✅ PASS          |
| Open the Logout Page                | Logout page is loaded successfully                     | ✅ PASS          |
| Open the specific perfume Page                | Page is loaded successfully                     | ✅ PASS          |
| Try to open non-existing page                | 404 page is loaded successfully                     | ✅ PASS          |
| Open the Add Perfume Page(authenticated)               | Add Perfume page is loaded successfully                     | ✅ PASS          |
| Register user with valid data              | Request is successfull                     | ✅ PASS          |
| Register user with invalid data              | Request is  not successfull                     | ✅ PASS          |
| Login user with valid data              | Request is successfull                     | ✅ PASS          |
| Login user with invalid data              | Request is  not successfull                     | ✅ PASS          |
| Add Perfume form filled in correctly              | Review created successfully                     | ✅ PASS          |
| Add Perfume form filled in incorrectly              | Mistake is pointed out                     | ✅ PASS          |
| Authenticated user views his own post              | Edit and Delete buttons are present                    | ✅ PASS          |
| Non-authenticated user views his own post              | Edit and Delete buttons aren't present                     | ✅ PASS          |
| Authenticated user views not own post              | Edit and Delete buttons aren't present                     | ✅ PASS          |
| Non-authenticated user tries to load /add_review/ page by typing it in             | User is taken to the Sign In page                     | ✅ PASS          |
| User tries to delete other persons post by typing in .../delete/'perfume_page'/              | Not able to, 403 page is successfully loaded                     | ✅ PASS          |
| Non-authenticated user tries to delete own post by typing in .../delete/'perfume_page'/              | Not able to, User is taken to login page                     | ✅ PASS          |
| Authenticated user clicks edit button              | Edit review form is loaded successfully                     | ✅ PASS          |
| Authenticated user clicks delete button              | Delete confirmation page is loaded successfully                     | ✅ PASS          |
| Authenticated user clicks Submit Changes button              | Edit review form is submited successfully                     | ✅ PASS          |
| Authenticated user clicks confirm button at Delete Confirmation page             | Perfume review is deleted successfully                     | ✅ PASS          |
| Sign Out button is clicked              | User is signed out successfully                     | ✅ PASS          |
| Social Network icons within footer are clicked              | Page in a new tab is loaded successfully                     | ✅ PASS          |