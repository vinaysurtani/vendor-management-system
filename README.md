# Vendor Management System

This is a system which covers a variety of features such as handling vendor profiles, tracking purchase orders as well as calculating vendor performance metrics.


## Features

- Vendor Profile Management:
    - Create, Retrieve, Update and Delete Vendor Profiles where you can store information such as name, contact details, address, and a unique vendor code.
- Purchase Order Tracking:
    - Create, Retrieve, Update and Delete Purchase Orders where you store fields like the PO Number, Vendor reference, order date, items, quantity and status.
    - You can also add the acknowledgement date of the order later when it will be checked on by the respective vendor.
- Vendor Performance Metrics:
    - Perform various checks on the vendors such as on-time delivery rate, average quality rating, average response time and fulfillment date and also check the history of these details with every purchase order.



## API Reference


#### Vendor Endpoints

| Endpoint | Method     | Description                |
| :-------- | :------- | :------------------------- |
| `/api/vendors/` | `GET` |  List all vendors. |
| `/api/vendors/` | `POST` | Create a new vendor. |
| `/api/vendors/{vendor_id}/` | `GET` |  Retrieve a specific vendor's details. |
| `/api/vendors/{vendor_id}/` | `PUT/PATCH` |  Update a vendor's details. |
| `/api/vendors/{vendor_id}/` | `DELETE` | Delete a vendor. |

#### Purchase Order Endpoints

| Endpoint | Method     | Description                |
| :-------- | :------- | :------------------------- |
| `/api/purchase-orders/` | `GET` |  List all purchase orders. |
| `/api/purchase-orders/` | `POST` |  Create a purchase order. |
| `/api/purchase-orders/{po_number}/` | `GET` |  Retrieve details of a specific purchase order. |
| `/api/purchase-orders/{po_number}/` | `PUT/PATCH` |  Update a purchase order. |
| `/api/purchase-orders/{po_number}/` | `DELETE` |  Delete a purchase order. |
| `/api/purchase-orders/{po_number}/acknowledge/` | `PUT/PATCH` |  Add the acknowledgement date for specific purchase order. |

#### Performance Metrics Endpoints

| Endpoint | Method     | Description                |
| :-------- | :------- | :------------------------- |
| `/api/vendors/{vendor_id}/performance/` | `GET` |  Retrieve a vendor's performance metrics. |

#### Login Endpoint

| Endpoint | Method     | Description                |
| :-------- | :------- | :------------------------- |
| `/api-auth/login/` | `POST` |  Enter login details, and routes to further API endpoints. |

## Installation and Running the application

- Clone the project, and navigate to the project folder.

```bash
  git clone https://github.com/vinaysurtani/vendor-management-system.git
```

- Create a Virtual Environment, where you can install the dependencies and then activate it with the below commands.

```bash
  python -m venv env
  source env/bin/activate
  # cd env\Source\activate for windows
```

- Install Project Dependencies

```bash
  pip install -r requirements.txt
```

- Then change directory to the project and apply the database migrations

```bash
python manage.py migrate
```


- To run the application, create a superuser and generate a token for the same so that the user is authorized to access the various endpoints of the applications

```bash
python manage.py createsuperuser
```
- Run the development server

```bash
python manage.py runserver
```

- After creating the user, you can generate the Token either from:
    - Django admin panel
    - ```python manage.py drf_create_token <username>```
    - From the endpoint ```/api/apitoken/``` by passing the username and password of the user in JSON format.