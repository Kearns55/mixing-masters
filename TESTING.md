# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation
### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| contact | [contact_form.html](https://github.com/Kearns55/mixing-masters/blob/main/contact/templates/contact/contact_form.html) |  https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcontact%2F | ![screenshot](documentation/validation/html-contact-contact_form.png) | 
| contact | [contact_success.html](https://github.com/Kearns55/mixing-masters/blob/main/contact/templates/contact/contact_success.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcontact%2Fsuccess%2F | ![screenshot](documentation/validation/html-contact-contact_success.png) |
| courses | [admin_dashboard.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/admin_dashboard.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2Fadmin-dashboard%2F | ![screenshot](documentation/validation/html-courses-admin_dashboard.png) | The trailing slash comes from djangos allauth. |
| courses | [cancel.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/cancel.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2Fcancel%2F | ![screenshot](documentation/validation/html-courses-cancel.png) | 
| courses | [course_detail.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/course_detail.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2F5%2F | ![screenshot](documentation/validation/html-courses-course_detail.png) | 
| courses | [course_list.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/course_list.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2F | ![screenshot](documentation/validation/html-courses-course_list.png) | 
| courses | [create_course.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/create_course.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2Fcreate-course%2F | ![screenshot](documentation/validation/html-courses-create_course.png) | The trailing slash comes from djangos crispy forms. |
| courses | [delete_course.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/delete_course.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2Fdelete-course%2F5%2F | ![screenshot](documentation/validation/html-courses-delete_course.png) | The trailing slash comes from djangos crispy forms. |
| courses | [delete_level.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/delete_level.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2Fdelete-level%2F3%2F | ![screenshot](documentation/validation/html-courses-delete_level.png) | The trailing slash comes from djangos crispy forms. |
| courses | [delete_supply.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/delete_supply.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2Fdelete-supply%2F1%2F | ![screenshot](documentation/validation/html-courses-delete_supply.png) | The trailing slash comes from djangos crispy forms. |
| courses | [my_courses.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/my_courses.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2Fmy-courses%2F | ![screenshot](documentation/validation/html-courses-my_courses.png) | The trailing slash comes from djangos crispy forms. | 
| courses | [success.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/success.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2Fsuccess%2F | ![screenshot](documentation/validation/html-courses-success.png) |  The trailing slash comes from djangos crispy forms. |
| courses | [update_course.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/update_course.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2Fupdate-course%2F5%2F | ![screenshot](documentation/validation/html-courses-update_course.png) | The trailing slash comes from djangos crispy forms. |
| courses | [update_level.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/update_level.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2Fupdate-level%2F3%2F | ![screenshot](documentation/validation/html-courses-update_level.png) | The trailing slash comes from djangos crispy forms. |
| courses | [update_supply.html](https://github.com/Kearns55/mixing-masters/blob/main/courses/templates/courses/update_supply.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Fcourses%2Fupdate-supply%2F1%2F | ![screenshot](documentation/validation/html-courses-update_supply.png) | The trailing slash comes from djangos crispy forms. |
| home | [index.html](https://github.com/Kearns55/mixing-masters/blob/main/home/templates/home/index.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2F | ![screenshot](documentation/validation/html-home-index.png) | 
| templates | [404.html](https://github.com/Kearns55/mixing-masters/blob/main/templates/errors/404.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2F404&checkerrorpages=yes | ![screenshot](documentation/validation/html-templates-404.png) |
| templates | [email_confirm.html](https://github.com/Kearns55/mixing-masters/blob/main/templates/account/email_confirm.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Faccounts%2Fconfirm-email%2F | ![screenshot](documentation/validation/html-templates-email_confirm.png) |
| templates | [login.html](https://github.com/Kearns55/mixing-masters/blob/main/templates/account/login.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Faccounts%2Flogin%2F | ![screenshot](documentation/validation/html-templates-login.png) | 
| templates | [logout.html](https://github.com/Kearns55/mixing-masters/blob/main/templates/account/logout.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Faccounts%2Flogout%2F | ![screenshot](documentation/validation/html-templates-logout.png) |
| templates | [signup.html](https://github.com/Kearns55/mixing-masters/blob/main/templates/account/signup.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Faccounts%2Fsignup%2F | ![screenshot](documentation/validation/html-templates-signup.png) | 
| templates | [verification_sent.html](https://github.com/Kearns55/mixing-masters/blob/main/templates/account/verification_sent.html) | https://validator.w3.org/nu/?doc=https%3A%2F%2Fmixing-masters-ee8e2a1f7802.herokuapp.com%2Faccounts%2Fconfirm-email%2F | ![screenshot](documentation/validation/html-templates-verification_sent.png) |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| static | [styles.css](https://github.com/Kearns55/mixing-masters/blob/main/static/css/styles.css) | ![screenshot](documentation/validation/css-static-styles.png) | 


### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot |
| --- | --- | --- | --- |
| contact | [admin.py](https://github.com/Kearns55/mixing-masters/blob/main/contact/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/contact/admin.py) | ![screenshot](documentation/validation/py-contact-admin.png) | 
| contact | [forms.py](https://github.com/Kearns55/mixing-masters/blob/main/contact/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/contact/forms.py) | ![screenshot](documentation/validation/py-contact-forms.png) | 
| contact | [models.py](https://github.com/Kearns55/mixing-masters/blob/main/contact/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/contact/models.py) | ![screenshot](documentation/validation/py-contact-models.png) |
| contact | [urls.py](https://github.com/Kearns55/mixing-masters/blob/main/contact/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/contact/urls.py) | ![screenshot](documentation/validation/py-contact-urls.png) | 
| contact | [views.py](https://github.com/Kearns55/mixing-masters/blob/main/contact/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/contact/views.py) | ![screenshot](documentation/validation/py-contact-views.png) |
| courses | [admin.py](https://github.com/Kearns55/mixing-masters/blob/main/courses/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/courses/admin.py) | ![screenshot](documentation/validation/py-courses-admin.png) |
| courses | [forms.py](https://github.com/Kearns55/mixing-masters/blob/main/courses/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/courses/forms.py) | ![screenshot](documentation/validation/py-courses-forms.png) | 
| courses | [models.py](https://github.com/Kearns55/mixing-masters/blob/main/courses/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/courses/models.py) | ![screenshot](documentation/validation/py-courses-models.png) |
| courses | [server.py](https://github.com/Kearns55/mixing-masters/blob/main/courses/server.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/courses/server.py) | ![screenshot](documentation/validation/py-courses-server.png) |
| courses | [urls.py](https://github.com/Kearns55/mixing-masters/blob/main/courses/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/courses/urls.py) | ![screenshot](documentation/validation/py-courses-urls.png) |
| courses | [views.py](https://github.com/Kearns55/mixing-masters/blob/main/courses/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/courses/views.py) | ![screenshot](documentation/validation/py-courses-views.png) |
| home | [urls.py](https://github.com/Kearns55/mixing-masters/blob/main/home/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/home/urls.py) | ![screenshot](documentation/validation/py-home-urls.png) |
| home | [views.py](https://github.com/Kearns55/mixing-masters/blob/main/home/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/home/views.py) | ![screenshot](documentation/validation/py-home-views.png) |
|  | [manage.py](https://github.com/Kearns55/mixing-masters/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/manage.py) | ![screenshot](documentation/validation/py--manage.png) |
| mixing_masters | [settings.py](https://github.com/Kearns55/mixing-masters/blob/main/mixing_masters/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/mixing_masters/settings.py) | ![screenshot](documentation/validation/py-mixing_masters-settings.png) |
| mixing_masters | [urls.py](https://github.com/Kearns55/mixing-masters/blob/main/mixing_masters/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/mixing_masters/urls.py) | ![screenshot](documentation/validation/py-mixing_masters-urls.png) |
| mixing_masters | [views.py](https://github.com/Kearns55/mixing-masters/blob/main/mixing_masters/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Kearns55/mixing-masters/main/mixing_masters/views.py) | ![screenshot](documentation/validation/py-mixing_masters-views.png) | 

## Responsiveness

I've tested my deployed project to check for responsiveness issues.

| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/responsiveness/mobile-register.png) | ![screenshot](documentation/responsiveness/brave-register.png) | ![screenshot](documentation/responsiveness/desktop-register.png) | Works as expected |
| Login | ![screenshot](documentation/responsiveness/mobile-login.png) | ![screenshot](documentation/responsiveness/brave-login.png) | ![screenshot](documentation/responsiveness/desktop-login.png) | Works as expected |
| Profile | ![screenshot](documentation/responsiveness/mobile-profile.png) | ![screenshot](documentation/responsiveness/brave-profile.png) | ![screenshot](documentation/responsiveness/desktop-profile.png) | Works as expected |
| Home | ![screenshot](documentation/responsiveness/mobile-home.png) | ![screenshot](documentation/responsiveness/brave-home.png) | ![screenshot](documentation/responsiveness/desktop-home.png) | Works as expected |
| Workshops | ![screenshot](documentation/responsiveness/mobile-workshops.png) | ![screenshot](documentation/responsiveness/brave-workshops.png) | ![screenshot](documentation/responsiveness/desktop-workshops.png) | Works as expected |
| Workshop Details | ![screenshot](documentation/responsiveness/mobile-workshop-details.png) | ![screenshot](documentation/responsiveness/brave-workshop-details.png) | ![screenshot](documentation/responsiveness/desktop-workshop-details.png) | Works as expected |
| Checkout | ![screenshot](documentation/responsiveness/mobile-checkout.png) | ![screenshot](documentation/responsiveness/brave-checkout.png) | ![screenshot](documentation/responsiveness/desktop-checkout.png) | Works as expected |
| Checkout Success | ![screenshot](documentation/responsiveness/mobile-checkout-success.png) | ![screenshot](documentation/responsiveness/brave-checkout-success.png) | ![screenshot](documentation/responsiveness/desktop-checkout-success.png) | Works as expected |
| Add workshop | ![screenshot](documentation/responsiveness/mobile-add-workshop.png) | ![screenshot](documentation/responsiveness/brave-add-workshop.png) | ![screenshot](documentation/responsiveness/desktop-add-workshop.png) | Works as expected |
| Edit workshop | ![screenshot](documentation/responsiveness/mobile-edit-workshop.png) | ![screenshot](documentation/responsiveness/brave-edit-workshop.png) | ![screenshot](documentation/responsiveness/desktop-edit-workshop.png) | Works as expected |
| Contact | ![screenshot](documentation/responsiveness/mobile-contact.png) | ![screenshot](documentation/responsiveness/brave-contact.png) | ![screenshot](documentation/responsiveness/desktop-contact.png) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/mobile-404.png) | ![screenshot](documentation/responsiveness/brave-404.png) | ![screenshot](documentation/responsiveness/desktop-404.png) | Works as expected |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page | Chrome | Brave | Safari | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/responsiveness/desktop-register.png) | ![screenshot](documentation/responsiveness/brave-register.png) | ![screenshot](documentation/responsiveness/mobile-register.png) | Works as expected |
| Login | ![screenshot](documentation/responsiveness/desktop-login.png) | ![screenshot](documentation/responsiveness/brave-login.png) | ![screenshot](documentation/responsiveness/mobile-login.png) | Works as expected |
| Profile | ![screenshot](documentation/responsiveness/desktop-profile.png) | ![screenshot](documentation/responsiveness/brave-profile.png) | ![screenshot](documentation/responsiveness/mobile-profile.png) | Works as expected |
| Home | ![screenshot](documentation/responsiveness/desktop-home.png) | ![screenshot](documentation/responsiveness/brave-home.png) | ![screenshot](documentation/responsiveness/mobile-home.png) | Works as expected |
| Workshops | ![screenshot](documentation/responsiveness/desktop-workshops.png) | ![screenshot](documentation/responsiveness/brave-workshops.png) | ![screenshot](documentation/responsiveness/mobile-workshops.png) | Works as expected |
| Workshop Details | ![screenshot](documentation/responsiveness/desktop-workshop-details.png) | ![screenshot](documentation/responsiveness/brave-workshop-details.png) | ![screenshot](documentation/responsiveness/mobile-workshop-details.png) | Works as expected |
| Checkout | ![screenshot](documentation/responsiveness/desktop-checkout.png) | ![screenshot](documentation/responsiveness/brave-checkout.png) | ![screenshot](documentation/responsiveness/mobile-checkout.png) | Works as expected |
| Checkout Success | ![screenshot](documentation/responsiveness/desktop-checkout-success.png) | ![screenshot](documentation/responsiveness/brave-checkout-success.png) | ![screenshot](documentation/responsiveness/mobile-checkout-success.png) | Works as expected |
| Add workshop | ![screenshot](documentation/responsiveness/desktop-add-workshop.png) | ![screenshot](documentation/responsiveness/brave-add-workshop.png) | ![screenshot](documentation/responsiveness/mobile-add-workshop.png) | Works as expected |
| Edit workshop | ![screenshot](documentation/responsiveness/desktop-edit-workshop.png) | ![screenshot](documentation/responsiveness/brave-edit-workshop.png) | ![screenshot](documentation/responsiveness/mobile-edit-workshop.png) | Works as expected |
| Contact | ![screenshot](documentation/responsiveness/desktop-contact.png) | ![screenshot](documentation/responsiveness/brave-contact.png) | ![screenshot](documentation/responsiveness/mobile-contact.png) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/desktop-404.png) | ![screenshot](documentation/responsiveness/brave-404.png) | ![screenshot](documentation/responsiveness/mobile-404.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Register | ![screenshot](documentation/lighthouse/mobile-register.png) | ![screenshot](documentation/lighthouse/desktop-register.png) |
| Login | ![screenshot](documentation/lighthouse/mobile-login.png) | ![screenshot](documentation/lighthouse/desktop-login.png) |
| Home | ![screenshot](documentation/lighthouse/mobile-home.png) | ![screenshot](documentation/lighthouse/desktop-home.png) |
| Workshops | ![screenshot](documentation/lighthouse/mobile-workshops.png) | ![screenshot](documentation/lighthouse/desktop-workshops.png) |
| Workshop Details | ![screenshot](documentation/lighthouse/mobile-workshop-details.png) | ![screenshot](documentation/lighthouse/desktop-workshop-details.png) |
| Checkout | ![screenshot](documentation/lighthouse/mobile-checkout.png) | ![screenshot](documentation/lighthouse/desktop-checkout.png) | Stripe's checkout page running very low lighthouse scores | 
| ![screenshot](documentation/lighthouse/low-lighthouse.png) |
| Checkout Success | ![screenshot](documentation/lighthouse/mobile-checkout-success.png) | ![screenshot](documentation/lighthouse/desktop-checkout-success.png) |
| Add workshop | ![screenshot](documentation/lighthouse/mobile-add-workshop.png) | ![screenshot](documentation/lighthouse/desktop-add-workshop.png) |
| Edit workshop | ![screenshot](documentation/lighthouse/mobile-edit-workshop.png) | ![screenshot](documentation/lighthouse/desktop-edit-workshop.png) |
| Contact | ![screenshot](documentation/lighthouse/mobile-contact.png) | ![screenshot](documentation/lighthouse/desktop-contact.png) |
| 404 | ![screenshot](documentation/lighthouse/mobile-404.png) | ![screenshot](documentation/lighthouse/desktop-404.png) |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Workshops | Feature is expected to allow users to browse workshops without registration. | Opened workshop pages as a guest user. | workshops were fully accessible without requiring registration. | ![screenshot](documentation/defensive/workshops.png) |
| | Feature is expected to show detailed workshop information. | Clicked on individual workshops to view details. | workshop details (description, price, image) were displayed correctly. | ![screenshot](documentation/defensive/workshop-details.png) |
| | Feature is expected to allow secure payment via Stripe. | Entered valid card details using Stripe at checkout. | Payment was processed securely, and an order confirmation page was displayed. | ![screenshot](documentation/defensive/stripe-payment.png) |
| | Feature is expected to send a confirmation email after purchase. | Completed a purchase and checked email inbox. | Confirmation email was received with order details. | ![screenshot](documentation/defensive/confirmation-email.png) |
| | Feature is expected to display an order confirmation page. | Completed a purchase. | Order confirmation page displayed successfully. | ![screenshot](documentation/defensive/order-confirmation.png) |
| Account Management | Feature is expected to allow returning customers to log in and view past orders. | Logged in as a returning customer and accessed order history. | Past orders were displayed correctly in the account section. | ![screenshot](documentation/defensive/order-history.png) |
| Admin Features | Feature is expected to allow the site owner to create new workshops. | Created new workshops with valid data (name, price, description, image, category). | workshops were added successfully and displayed on the site. | ![screenshot](documentation/defensive/create-workshop.png) |
| | Feature is expected to allow the site owner to update workshop details. | Edited workshop details as an admin user. | workshop updates were saved and displayed correctly. | ![screenshot](documentation/defensive/update-workshop.png) |
| | Feature is expected to allow the site owner to delete workshops. | Deleted a workshop from the inventory. | workshop was removed successfully from the site, after being prompted to confirm first. | ![screenshot](documentation/defensive/delete-workshop.png) |
| 404 Error Page | Feature is expected to display a 404 error page for non-existent pages. | Navigated to an invalid URL (e.g., `/test`). | A custom 404 error page was displayed as expected. | ![screenshot](documentation/defensive/404.png) |

## User Story Testing

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a visitor | I would like to browse available mixology courses  | so that I can decide if i want to enroll. | ![screenshot](documentation/features/workshops-list.png) |
| As a guest user | I would like to create an account | so that I can complete my purchase and track my order history. | ![screenshot](documentation/features/register.png) |
| As a customer | I would like to click on individual workshops to view more details (description, price, image, etc.) | so that I can make an informed decision about my purchase. | ![screenshot](documentation/features/workshop-details.png) |
| As a customer | I would like to receive a confirmation email after my purchase | so that I can have a record of my transaction and order details. | ![screenshot](documentation/features/confirmation-email.png) |
| As a customer | I would like to see an order confirmation page after completing my purchase | so that I know my order has been successfully placed. | ![screenshot](documentation/features/order-confirmation.png) |
| As a customer | I would like to securely enter my card details using Stripe at checkout | so that I can feel confident my payment information is protected. | ![screenshot](documentation/features/checkout.png) |
| As a returning customer | I would like to be able to log in and view the workshops I'm enrolled in | so that I can track my previous purchases. | ![screenshot](documentation/features/order-history.png) |
| As a site owner | I would like to create new workshops with a name, description, price, images, location, supplies and levels | so that I can add additional items to the sites inventory. | ![screenshot](documentation/features/create-workshop.png) |
| As a site owner | I would like to update workshop details (name, price, description, image etc.) at any time | so that I can keep my workshop listings accurate and up to date. | ![screenshot](documentation/features/update-workshop.png) |
| As a site owner | I would like to delete workshops that are no longer available or relevant | so that I can maintain a clean and accurate inventory. | ![screenshot](documentation/features/delete-workshop.png) |
| As a user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. | ![screenshot](documentation/features/404.png) |


## Bugs

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/Kearns55/mixing-masters?query=is%3Aissue%20is%3Aclosed%20label%3Abug&label=Fixed%20Bugs&color=green)](https://www.github.com/Kearns55/mixing-masters/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/Kearns55/mixing-masters/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/Kearns55/mixing-masters/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)

### Unfixed Bugs


[![GitHub issue custom search](https://img.shields.io/github/issues-search/Kearns55/mixing-masters?query=is%3Aissue%2Bis%3Aopen%2Blabel%3Abug&label=Unfixed%20Bugs&color=red)](https://www.github.com/Kearns55/mixing-masters/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

Any remaining open issues can be tracked [here](https://www.github.com/Kearns55/mixing-masters/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

![screenshot](documentation/bugs/gh-issues-open.png)

### Known Issues

| Issue | Screenshot |
| --- | --- |
| The project is designed to be responsive from `375px` and upwards, in line with the material taught on the course LMS. Minor layout inconsistencies may occur on extra-wide (e.g. 4k/8k monitors), or smart-display devices (e.g. Nest Hub, Smart Watches, Gameboy Color, etc.), as these resolutions are outside the project’s scope, as taught by Code Institute. | ![screenshot](documentation/issues/poor-responsiveness.png) |
| With a known order-number, users can brute-force "checkout_success.html" and see potentially sensitive information. | ![screenshot](documentation/issues/checkout-success.png) |

> [!IMPORTANT]  
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

