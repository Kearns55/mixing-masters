# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation
### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| contact | [contact_form.html](https://github.com/Kearns55/mixing-masters/blob/main/contact/templates/contact/contact_form.html) |  https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcontact%2F | ![screenshot](documentation/validation/html-contact-contact_form.PNG) | 
| contact | [contact_success.html](https://github.com/Kearns55/mixing-masters/blob/main/contact/templates/contact/contact_success.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcontact%2Fsuccess%2F | ![screenshot](documentation/validation/html-contact-contact_success.PNG) |
| courses | [admin_dashboard.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/admin_dashboard.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2Fadmin-dashboard%2F | ![screenshot](documentation/validation/html-courses-admin_dashboard.PNG) | The trailing slash comes from djangos allauth. |
| courses | [cancel.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/cancel.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2Fcancel%2F | ![screenshot](documentation/validation/html-courses-cancel.PNG) | 
| courses | [course_detail.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/course_detail.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2F5%2F | ![screenshot](documentation/validation/html-courses-course_detail.PNG) | 
| courses | [course_list.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/course_list.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2F | ![screenshot](documentation/validation/html-courses-course_list.PNG) | 
| courses | [create_course.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/create_course.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2Fcreate-course%2F | ![screenshot](documentation/validation/html-courses-create_course.PNG) | The trailing slash comes from djangos crispy forms. |
| courses | [delete_course.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/delete_course.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2Fdelete-course%2F5%2F | ![screenshot](documentation/validation/html-courses-delete_course.PNG) | The trailing slash comes from djangos crispy forms. |
| courses | [delete_level.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/delete_level.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2Fdelete-level%2F3%2F | ![screenshot](documentation/validation/html-courses-delete_level.PNG) | The trailing slash comes from djangos crispy forms. |
| courses | [delete_supply.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/delete_supply.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2Fdelete-supply%2F1%2F | ![screenshot](documentation/validation/html-courses-delete_supply.PNG) | The trailing slash comes from djangos crispy forms. |
| courses | [my_courses.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/my_courses.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2Fmy-courses%2F | ![screenshot](documentation/validation/html-courses-my_courses.PNG) | The trailing slash comes from djangos crispy forms. | 
| courses | [success.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/success.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2Fsuccess%2F | ![screenshot](documentation/validation/html-courses-success.PNG) |  The trailing slash comes from djangos crispy forms. |
| courses | [update_course.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/update_course.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2Fupdate-course%2F5%2F | ![screenshot](documentation/validation/html-courses-update_course.PNG) | The trailing slash comes from djangos crispy forms. |
| courses | [update_level.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/update_level.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2Fupdate-level%2F3%2F | ![screenshot](documentation/validation/html-courses-update_level.PNG) | The trailing slash comes from djangos crispy forms. |
| courses | [update_supply.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/update_supply.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2Fupdate-supply%2F1%2F | ![screenshot](documentation/validation/html-courses-update_supply.PNG) | The trailing slash comes from djangos crispy forms. |
| home | [index.html](https://github.com/Kearns55/mixing-masters/blob/main/home/templates/home/index.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2F | ![screenshot](documentation/validation/html-home-index.PNG) | 
| templates | [404.html](https://github.com/Kearns55/mixing-masters/blob/main/templates/errors/404.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2F404&checkerrorpages=yes | ![screenshot](documentation/validation/html-templates-404.PNG) |
| templates | [email_confirm.html](https://github.com/Kearns55/mixing-masters/blob/main/templates/account/email_confirm.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Faccounts%2Fconfirm-email%2F | ![screenshot](documentation/validation/html-templates-email_confirm.PNG) |
| templates | [login.html](https://github.com/Kearns55/mixing-masters/blob/main/templates/account/login.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Faccounts%2Flogin%2F | ![screenshot](documentation/validation/html-templates-login.PNG) | 
| templates | [logout.html](https://github.com/Kearns55/mixing-masters/blob/main/templates/account/logout.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Faccounts%2Flogout%2F | ![screenshot](documentation/validation/html-templates-logout.PNG) |
| templates | [signup.html](https://github.com/Kearns55/mixing-masters/blob/main/templates/account/signup.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Faccounts%2Fsignup%2F | ![screenshot](documentation/validation/html-templates-signup.PNG) | 
| templates | [verification_sent.html](https://github.com/Kearns55/mixing-masters/blob/main/templates/account/verification_sent.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Faccounts%2Fconfirm-email%2F | ![screenshot](documentation/validation/html-templates-verification_sent.PNG) |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot |
| --- | --- | --- | --- | 
| static | [styles.css] | (https://github.com/Kearns55/mixing-masters/blob/main/static/css/styles.css) | ![screenshot](documentation/validation/css-static-styles.PNG) | 


### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot |
| --- | --- | --- | --- |
| contact | [admin.py](https://github.com/Kearns55/mixing-masters/blob/main/contact/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/contact/admin.py) | ![screenshot](documentation/validation/py-contact-admin.PNG) | 
| contact | [forms.py](https://github.com/Kearns55/mixing-masters/blob/main/contact/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/contact/forms.py) | ![screenshot](documentation/validation/py-contact-forms.PNG) | 
| contact | [models.py](https://github.com/Kearns55/mixing-masters/blob/main/contact/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/contact/models.py) | ![screenshot](documentation/validation/py-contact-models.PNG) |
| contact | [urls.py](https://github.com/Kearns55/mixing-masters/blob/main/contact/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/contact/urls.py) | ![screenshot](documentation/validation/py-contact-urls.PNG) | 
| contact | [views.py](https://github.com/Kearns55/mixing-masters/blob/main/contact/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/contact/views.py) | ![screenshot](documentation/validation/py-contact-views.PNG) |
| courses | [admin.py](https://github.com/Kearns55/mixing-masters/blob/main/courses/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/courses/admin.py) | ![screenshot](documentation/validation/py-courses-admin.PNG) |
| courses | [forms.py](https://github.com/Kearns55/mixing-masters/blob/main/courses/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/courses/forms.py) | ![screenshot](documentation/validation/py-courses-forms.PNG) | 
| courses | [models.py](https://github.com/Kearns55/mixing-masters/blob/main/courses/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/courses/models.py) | ![screenshot](documentation/validation/py-courses-models.PNG) |
| courses | [server.py](https://github.com/Kearns55/mixing-masters/blob/main/courses/server.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/courses/server.py) | ![screenshot](documentation/validation/py-courses-server.PNG) |
| courses | [urls.py](https://github.com/Kearns55/mixing-masters/blob/main/courses/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/courses/urls.py) | ![screenshot](documentation/validation/py-courses-urls.PNG) |
| courses | [views.py](https://github.com/Kearns55/mixing-masters/blob/main/courses/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/courses/views.py) | ![screenshot](documentation/validation/py-courses-views.PNG) |
| home | [urls.py](https://github.com/Kearns55/mixing-masters/blob/main/home/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/home/urls.py) | ![screenshot](documentation/validation/py-home-urls.PNG) |
| home | [views.py](https://github.com/Kearns55/mixing-masters/blob/main/home/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/home/views.py) | ![screenshot](documentation/validation/py-home-views.PNG) |
|  | [manage.py](https://github.com/Kearns55/mixing-masters/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/manage.py) | ![screenshot](documentation/validation/py--manage.PNG) |
| mixing_masters | [settings.py](https://github.com/Kearns55/mixing-masters/blob/main/mixing_masters/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/mixing_masters/settings.py) | ![screenshot](documentation/validation/py-mixing_masters-settings.PNG) |
| mixing_masters | [urls.py](https://github.com/Kearns55/mixing-masters/blob/main/mixing_masters/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/mixing_masters/urls.py) | ![screenshot](documentation/validation/py-mixing_masters-urls.PNG) |
| mixing_masters | [views.py](https://github.com/Kearns55/mixing-masters/blob/main/mixing_masters/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/mixing_masters/views.py) | ![screenshot](documentation/validation/py-mixing_masters-views.PNG) | 

## Responsiveness

I've tested my deployed project to check for responsiveness issues.

| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/responsiveness/mobile-register.PNG) | ![screenshot](documentation/responsiveness/brave-register.PNG) | ![screenshot](documentation/responsiveness/desktop-register.PNG) | Works as expected |
| Login | ![screenshot](documentation/responsiveness/mobile-login.PNG) | ![screenshot](documentation/responsiveness/brave-login.PNG) | ![screenshot](documentation/responsiveness/desktop-login.PNG) | Works as expected |
| Profile | ![screenshot](documentation/responsiveness/mobile-profile.PNG) | ![screenshot](documentation/responsiveness/brave-profile.PNG) | ![screenshot](documentation/responsiveness/desktop-profile.PNG) | Works as expected |
| Home | ![screenshot](documentation/responsiveness/mobile-home.PNG) | ![screenshot](documentation/responsiveness/brave-home.PNG) | ![screenshot](documentation/responsiveness/desktop-home.PNG) | Works as expected |
| Workshops | ![screenshot](documentation/responsiveness/mobile-workshops.PNG) | ![screenshot](documentation/responsiveness/brave-workshops.PNG) | ![screenshot](documentation/responsiveness/desktop-workshops.PNG) | Works as expected |
| Workshop Details | ![screenshot](documentation/responsiveness/mobile-workshop-details.PNG) | ![screenshot](documentation/responsiveness/brave-workshop-details.PNG) | ![screenshot](documentation/responsiveness/desktop-workshop-details.PNG) | Works as expected |
| Checkout | ![screenshot](documentation/responsiveness/mobile-checkout.PNG) | ![screenshot](documentation/responsiveness/brave-checkout.PNG) | ![screenshot](documentation/responsiveness/desktop-checkout.PNG) | Works as expected |
| Checkout Success | ![screenshot](documentation/responsiveness/mobile-checkout-success.PNG) | ![screenshot](documentation/responsiveness/brave-checkout-success.PNG) | ![screenshot](documentation/responsiveness/desktop-checkout-success.PNG) | Works as expected |
| Add workshop | ![screenshot](documentation/responsiveness/mobile-add-workshop.PNG) | ![screenshot](documentation/responsiveness/brave-add-workshop.PNG) | ![screenshot](documentation/responsiveness/desktop-add-workshop.PNG) | Works as expected |
| Edit workshop | ![screenshot](documentation/responsiveness/mobile-edit-workshop.PNG) | ![screenshot](documentation/responsiveness/brave-edit-workshop.PNG) | ![screenshot](documentation/responsiveness/desktop-edit-workshop.PNG) | Works as expected |
| Contact | ![screenshot](documentation/responsiveness/mobile-contact.PNG) | ![screenshot](documentation/responsiveness/brave-contact.PNG) | ![screenshot](documentation/responsiveness/desktop-contact.PNG) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/mobile-404.PNG) | ![screenshot](documentation/responsiveness/brave-404.PNG) | ![screenshot](documentation/responsiveness/desktop-404.PNG) | Works as expected |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page | Chrome | Brave | Safari | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/responsiveness/desktop-register.PNG) | ![screenshot](documentation/responsiveness/brave-register.PNG) | ![screenshot](documentation/responsiveness/mobile-register.PNG) | Works as expected |
| Login | ![screenshot](documentation/responsiveness/desktop-login.PNG) | ![screenshot](documentation/responsiveness/brave-login.PNG) | ![screenshot](documentation/responsiveness/mobile-login.PNG) | Works as expected |
| Profile | ![screenshot](documentation/responsiveness/desktop-profile.PNG) | ![screenshot](documentation/responsiveness/brave-profile.PNG) | ![screenshot](documentation/responsiveness/mobile-profile.PNG) | Works as expected |
| Home | ![screenshot](documentation/responsiveness/desktop-home.PNG) | ![screenshot](documentation/responsiveness/brave-home.PNG) | ![screenshot](documentation/responsiveness/mobile-home.PNG) | Works as expected |
| Workshops | ![screenshot](documentation/responsiveness/desktop-workshops.PNG) | ![screenshot](documentation/responsiveness/brave-workshops.PNG) | ![screenshot](documentation/responsiveness/mobile-workshops.PNG) | Works as expected |
| Workshop Details | ![screenshot](documentation/responsiveness/desktop-workshop-details.PNG) | ![screenshot](documentation/responsiveness/brave-workshop-details.PNG) | ![screenshot](documentation/responsiveness/mobile-workshop-details.PNG) | Works as expected |
| Checkout | ![screenshot](documentation/responsiveness/desktop-checkout.PNG) | ![screenshot](documentation/responsiveness/brave-checkout.PNG) | ![screenshot](documentation/responsiveness/mobile-checkout.PNG) | Works as expected |
| Checkout Success | ![screenshot](documentation/responsiveness/desktop-checkout-success.PNG) | ![screenshot](documentation/responsiveness/brave-checkout-success.PNG) | ![screenshot](documentation/responsiveness/mobile-checkout-success.PNG) | Works as expected |
| Add workshop | ![screenshot](documentation/responsiveness/desktop-add-workshop.PNG) | ![screenshot](documentation/responsiveness/brave-add-workshop.PNG) | ![screenshot](documentation/responsiveness/mobile-add-workshop.PNG) | Works as expected |
| Edit workshop | ![screenshot](documentation/responsiveness/desktop-edit-workshop.PNG) | ![screenshot](documentation/responsiveness/brave-edit-workshop.PNG) | ![screenshot](documentation/responsiveness/mobile-edit-workshop.PNG) | Works as expected |
| Contact | ![screenshot](documentation/responsiveness/desktop-contact.PNG) | ![screenshot](documentation/responsiveness/brave-contact.PNG) | ![screenshot](documentation/responsiveness/mobile-contact.PNG) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/desktop-404.PNG) | ![screenshot](documentation/responsiveness/brave-404.PNG) | ![screenshot](documentation/responsiveness/mobile-404.PNG) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/lighthouse/mobile-register.PNG) | ![screenshot](documentation/lighthouse/desktop-register.PNG) |
| Login | ![screenshot](documentation/lighthouse/mobile-login.PNG) | ![screenshot](documentation/lighthouse/desktop-login.PNG) |
| Home | ![screenshot](documentation/lighthouse/mobile-home.PNG) | ![screenshot](documentation/lighthouse/desktop-home.PNG) |
| Workshops | ![screenshot](documentation/lighthouse/mobile-workshops.PNG) | ![screenshot](documentation/lighthouse/desktop-workshops.PNG) |
| Workshop Details | ![screenshot](documentation/lighthouse/mobile-workshop-details.PNG) | ![screenshot](documentation/lighthouse/desktop-workshop-details.PNG) |
| Checkout | ![screenshot](documentation/lighthouse/mobile-checkout.PNG) | ![screenshot](documentation/lighthouse/desktop-checkout.PNG) | ![screenshot](documentation/lighthouse/low-lighthouse.PNG) | Stripe's checkout page running very low lighthouse scores |
| Checkout Success | ![screenshot](documentation/lighthouse/mobile-checkout-success.PNG) | ![screenshot](documentation/lighthouse/desktop-checkout-success.PNG) |
| Add workshop | ![screenshot](documentation/lighthouse/mobile-add-workshop.PNG) | ![screenshot](documentation/lighthouse/desktop-add-workshop.PNG) |
| Edit workshop | ![screenshot](documentation/lighthouse/mobile-edit-workshop.PNG) | ![screenshot](documentation/lighthouse/desktop-edit-workshop.PNG) |
| Contact | ![screenshot](documentation/lighthouse/mobile-contact.PNG) | ![screenshot](documentation/lighthouse/desktop-contact.PNG) |
| 404 | ![screenshot](documentation/lighthouse/mobile-404.PNG) | ![screenshot](documentation/lighthouse/desktop-404.PNG) |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Workshops | Feature is expected to allow users to browse workshops without registration. | Opened workshop pages as a guest user. | workshops were fully accessible without requiring registration. | ![screenshot](documentation/defensive/workshops.PNG) |
| | Feature is expected to show detailed workshop information. | Clicked on individual workshops to view details. | workshop details (description, price, image) were displayed correctly. | ![screenshot](documentation/defensive/workshop-details.PNG) |
| | Feature is expected to allow secure payment via Stripe. | Entered valid card details using Stripe at checkout. | Payment was processed securely, and an order confirmation page was displayed. | ![screenshot](documentation/defensive/stripe-payment.PNG) |
| | Feature is expected to send a confirmation email after purchase. | Completed a purchase and checked email inbox. | Confirmation email was received with order details. | ![screenshot](documentation/defensive/confirmation-email.PNG) |
| | Feature is expected to display an order confirmation page. | Completed a purchase. | Order confirmation page displayed successfully. | ![screenshot](documentation/defensive/order-confirmation.PNG) |
| Account Management | Feature is expected to allow returning customers to log in and view past orders. | Logged in as a returning customer and accessed order history. | Past orders were displayed correctly in the account section. | ![screenshot](documentation/defensive/order-history.PNG) |
| Admin Features | Feature is expected to allow the site owner to create new workshops. | Created new workshops with valid data (name, price, description, image, category). | workshops were added successfully and displayed on the site. | ![screenshot](documentation/defensive/create-workshop.PNG) |
| | Feature is expected to allow the site owner to update workshop details. | Edited workshop details as an admin user. | workshop updates were saved and displayed correctly. | ![screenshot](documentation/defensive/update-workshop.PNG) |
| | Feature is expected to allow the site owner to delete workshops. | Deleted a workshop from the inventory. | workshop was removed successfully from the site, after being prompted to confirm first. | ![screenshot](documentation/defensive/delete-workshop.PNG) |
| 404 Error Page | Feature is expected to display a 404 error page for non-existent pages. | Navigated to an invalid URL (e.g., `/test`). | A custom 404 error page was displayed as expected. | ![screenshot](documentation/defensive/404.PNG) |

## User Story Testing

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a visitor | I would like to browse available mixology courses  | so that I can decide if i want to enroll. | ![screenshot](documentation/features/workshops-list.PNG) |
| As a guest user | I would like to create an account | so that I can complete my purchase and track my order history. | ![screenshot](documentation/features/register.PNG) |
| As a customer | I would like to click on individual workshops to view more details (description, price, image, etc.) | so that I can make an informed decision about my purchase. | ![screenshot](documentation/features/workshop-details.PNG) |
| As a customer | I would like to receive a confirmation email after my purchase | so that I can have a record of my transaction and order details. | ![screenshot](documentation/features/confirmation-email.PNG) |
| As a customer | I would like to see an order confirmation page after completing my purchase | so that I know my order has been successfully placed. | ![screenshot](documentation/features/order-confirmation.PNG) |
| As a customer | I would like to securely enter my card details using Stripe at checkout | so that I can feel confident my payment information is protected. | ![screenshot](documentation/features/checkout.PNG) |
| As a returning customer | I would like to be able to log in and view the workshops I'm enrolled in | so that I can track my previous purchases. | ![screenshot](documentation/features/order-history.PNG) |
| As a site owner | I would like to create new workshops with a name, description, price, images, location, supplies and levels | so that I can add additional items to the sites inventory. | ![screenshot](documentation/features/create-workshop.PNG) |
| As a site owner | I would like to update workshop details (name, price, description, image etc.) at any time | so that I can keep my workshop listings accurate and up to date. | ![screenshot](documentation/features/update-workshop.PNG) |
| As a site owner | I would like to delete workshops that are no longer available or relevant | so that I can maintain a clean and accurate inventory. | ![screenshot](documentation/features/delete-workshop.PNG) |
| As a user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. | ![screenshot](documentation/features/404.PNG) |


## Bugs

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/Kearns55/mixing-masters?query=is%3Aissue%20is%3Aclosed%20label%3Abug&label=Fixed%20Bugs&color=green)](https://www.github.com/Kearns55/mixing-masters/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/Kearns55/mixing-masters/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/Kearns55/mixing-masters/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.PNG)

### Known Issues

| Issue | Screenshot |
| --- | --- |
| The project is designed to be responsive from `375px` and upwards, in line with the material taught on the course LMS. Minor layout inconsistencies may occur on extra-wide (e.g. 4k/8k monitors), or smart-display devices (e.g. Nest Hub, Smart Watches, Gameboy Color, etc.), as these resolutions are outside the project’s scope, as taught by Code Institute. | ![screenshot](documentation/issues/poor-responsiveness.PNG) |
| With a known order-number, users can brute-force "checkout_success.html" and see potentially sensitive information. | ![screenshot](documentation/issues/checkout-success.PNG) |

> [!IMPORTANT]  
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

