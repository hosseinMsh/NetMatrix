### **API Documentation**

#### **1. User API**

##### **1.1. Create User**
- **Endpoint**: `POST /api/users/`
- **Request Body**:
```json
{
  "username": "new_user",
  "email": "user@example.com",
  "password": "securepassword",
  "is_admin": false,
  "phone_number": "1234567890",
  "level": 1
}
```
- **Response**:
```json
{
  "id": 1,
  "username": "new_user",
  "email": "user@example.com",
  "is_admin": false,
  "phone_number": "1234567890",
  "created_at": "2023-10-01T12:00:00Z",
  "updated_at": "2023-10-01T12:00:00Z"
}
```

##### **1.2. List Users**
- **Endpoint**: `GET /api/users/`
- **Response**:
```json
[
  {
    "id": 1,
    "username": "new_user",
    "email": "user@example.com",
    "is_admin": false,
    "phone_number": "1234567890",
    "created_at": "2023-10-01T12:00:00Z",
    "updated_at": "2023-10-01T12:00:00Z"
  }
]
```

##### **1.3. Retrieve User**
- **Endpoint**: `GET /api/users/{id}/`
- **Response**:
```json
{
  "id": 1,
  "username": "new_user",
  "email": "user@example.com",
  "is_admin": false,
  "phone_number": "1234567890",
  "created_at": "2023-10-01T12:00:00Z",
  "updated_at": "2023-10-01T12:00:00Z"
}
```

##### **1.4. Update User**
- **Endpoint**: `PUT /api/users/{id}/`
- **Request Body**:
```json
{
  "username": "updated_user",
  "email": "updated@example.com",
  "is_admin": true,
  "phone_number": "0987654321",
  "level": 2
}
```
- **Response**:
```json
{
  "id": 1,
  "username": "updated_user",
  "email": "updated@example.com",
  "is_admin": true,
  "phone_number": "0987654321",
  "created_at": "2023-10-01T12:00:00Z",
  "updated_at": "2023-10-01T12:00:00Z"
}
```

##### **1.5. Delete User**
- **Endpoint**: `DELETE /api/users/{id}/`
- **Response**:
```json
{
  "detail": "User  deleted successfully."
}
```

---

#### **2. Virtual Machine API**

##### **2.1. Create Virtual Machine**
- **Endpoint**: `POST /api/virtualmachines/`
- **Request Body**:
```json
{
  "name": "VM1",
  "technical_responsible": 1,
  "legal_responsible": 2
}
```
- **Response**:
```json
{
  "id": 1,
  "name": "VM1",
  "technical_responsible": 1,
  "legal_responsible": 2,
  "created_at": "2023-10-01T12:00:00Z",
  "updated_at": "2023-10-01T12:00:00Z"
}
```

##### **2.2. List Virtual Machines**
- **Endpoint**: `GET /api/virtualmachines/`
- **Response**:
```json
[
  {
    "id": 1,
    "name": "VM1",
    "technical_responsible": 1,
    "legal_responsible": 2,
    "created_at": "2023-10-01T12:00:00Z",
    "updated_at": "2023-10-01T12:00:00Z"
  }
]
```

##### **2.3. Retrieve Virtual Machine**
- **Endpoint**: `GET /api/virtualmachines/{id}/`
- **Response**:
```json
{
  "id": 1,
  "name ": "VM1",
  "technical_responsible": 1,
  "legal_responsible": 2,
  "created_at": "2023-10-01T12:00:00Z",
  "updated_at": "2023-10-01T12:00:00Z"
}
```

##### **2.4. Update Virtual Machine**
- **Endpoint**: `PUT /api/virtualmachines/{id}/`
- **Request Body**:
```json
{
  "name": "Updated_VM",
  "technical_responsible": 1,
  "legal_responsible": 3
}
```
- **Response**:
```json
{
  "id": 1,
  "name": "Updated_VM",
  "technical_responsible": 1,
  "legal_responsible": 3,
  "created_at": "2023-10-01T12:00:00Z",
  "updated_at": "2023-10-01T12:00:00Z"
}
```

##### **2.5. Delete Virtual Machine**
- **Endpoint**: `DELETE /api/virtualmachines/{id}/`
- **Response**:
```json
{
  "detail": "Virtual Machine deleted successfully."
}
```

---

#### **3. Server API**

##### **3.1. Create Server**
- **Endpoint**: `POST /api/servers/`
- **Request Body**:
```json
{
  "name": "Server1",
  "internal_ip": "192.168.1.1",
  "public_ip": "203.0.113.1",
  "virtual_machine": 1,
  "owner": 1,
  "open_ports": [80, 443],
  "access_status": "active"
}
```
- **Response**:
```json
{
  "id": 1,
  "name": "Server1",
  "internal_ip": "192.168.1.1",
  "public_ip": "203.0.113.1",
  "virtual_machine": 1,
  "owner": 1,
  "open_ports": [80, 443],
  "access_status": "active",
  "created_at": "2023-10-01T12:00:00Z",
  "updated_at": "2023-10-01T12:00:00Z"
}
```

##### **3.2. List Servers**
- **Endpoint**: `GET /api/servers/`
- **Response**:
```json
[
  {
    "id": 1,
    "name": "Server1",
    "internal_ip": "192.168.1.1",
    "public_ip": "203.0.113.1",
    "virtual_machine": 1,
    "owner": 1,
    "open_ports": [80, 443],
    "access_status": "active",
    "created_at": "2023-10-01T12:00:00Z",
    "updated_at": "2023-10-01T12:00:00Z"
  }
]
```

##### **3.3. Retrieve Server**
- **Endpoint**: `GET /api/servers/{id}/`
- **Response**:
```json
{
  "id": 1,
  "name": "Server1",
  "internal_ip": "192.168.1.1",
  "public_ip": "203.0.113.1",
  "virtual_machine": 1,
  "owner": 1,
  "open_ports": [80, 443],
  "access_status": "active",
  "created_at": "2023-10-01T12:00:00Z",
  "updated_at": "2023-10-01T12:00:00Z"
}
```

##### **3.4. Update Server**
- **Endpoint**: `PUT /api/servers/{id}/`
- **Request Body**:
```json
{
  "name": "Updated_Server",
  "internal_ip": "192.168.1.2",
  "public_ip": "203.0.113.2",
  "virtual_machine": 1,
  "owner": 1,
  "open_ports": [22, 80],
  "access_status": "inactive"
}
```
- **Response**:
```json
{
  "id": 1,
  "name": "Updated_Server",
  "internal_ip": "192.168.1.2",
  "public_ip": "203.0.113.2",
  "virtual_machine": 1,
  "owner": 1,
  "open_ports": [22, 80],
  "access_status": "inactive",
  "created_at": "2023-10- 01T12:00:00Z",
  "updated_at": "2023-10-01T12:00:00Z"
}
```

##### **3.5. Delete Server**
- **Endpoint**: `DELETE /api/servers/{id}/`
- **Response**:
```json
{
  "detail": "Server deleted successfully."
}
```

---

#### **4. Domain API**

##### **4.1. Create Domain**
- **Endpoint**: `POST /api/domains/`
- **Request Body**:
```json
{
  "name": "example.com",
  "ssl_expiration_date": "2024-10-01",
  "server": 1,
  "owner": 1
}
```
- **Response**:
```json
{
  "id": 1,
  "name": "example.com",
  "ssl_expiration_date": "2024-10-01",
  "server": 1,
  "owner": 1,
  "created_at": "2023-10-01T12:00:00Z",
  "updated_at": "2023-10-01T12:00:00Z"
}
```

##### **4.2. List Domains**
- **Endpoint**: `GET /api/domains/`
- **Response**:
```json
[
  {
    "id": 1,
    "name": "example.com",
    "ssl_expiration_date": "2024-10-01",
    "server": 1,
    "owner": 1,
    "created_at": "2023-10-01T12:00:00Z",
    "updated_at": "2023-10-01T12:00:00Z"
  }
]
```

##### **4.3. Retrieve Domain**
- **Endpoint**: `GET /api/domains/{id}/`
- **Response**:
```json
{
  "id": 1,
  "name": "example.com",
  "ssl_expiration_date": "2024-10-01",
  "server": 1,
  "owner": 1,
  "created_at": "2023-10-01T12:00:00Z",
  "updated_at": "2023-10-01T12:00:00Z"
}
```

##### **4.4. Update Domain**
- **Endpoint**: `PUT /api/domains/{id}/`
- **Request Body**:
```json
{
  "name": "updated-example.com",
  "ssl_expiration_date": "2025-10-01",
  "server": 1,
  "owner": 2
}
```
- **Response**:
```json
{
  "id": 1,
  "name": "updated-example.com",
  "ssl_expiration_date": "2025-10-01",
  "server": 1,
  "owner": 2,
  "created_at": "2023-10-01T12:00:00Z",
  "updated_at": "2023-10-01T12:00:00Z"
}
```

##### **4.5. Delete Domain**
- **Endpoint**: `DELETE /api/domains/{id}/`
- **Response**:
```json
{
  "detail": "Domain deleted successfully."
}
```

---

#### **5. History API**

##### **5.1. Create History Entry**
- **Endpoint**: `POST /api/history/`
- **Request Body**:
```json
{
  "server": 1,
  "status": "active",
  "notes": "Server is running smoothly."
}
```
- **Response**:
```json
{
  "id": 1,
  "server": 1,
  "status": "active",
  "timestamp": "2023-10-01T12:00:00Z",
  "notes": "Server is running smoothly."
}
```

##### **5.2. List History Entries**
- **Endpoint**: `GET /api/history/`
- **Response**:
```json
[
  {
    "id": 1,
    "server": 1,
    "status": "active",
    "timestamp": "2023-10-01T12:00:00Z",
    "notes": "Server is running smoothly."
  }
]
```

##### **5.3. Retrieve History Entry**
- **Endpoint**: `GET /api/history/{id}/`
- **Response**:
```json
{
  "id": 1,
  "server": 1,
  "status": "active",
  "timestamp": "2023-10-01T12:00:00Z",
  "notes": "Server is running smoothly."
}
```

##### **5.4. Update History Entry - **Endpoint**: `PUT /api/history/{id}/`
- **Request Body**:
```json
{
  "server": 1,
  "status": "inactive",
  "notes": "Server is currently down for maintenance."
}
```
- **Response**:
```json
{
  "id": 1,
  "server": 1,
  "status": "inactive",
  "timestamp": "2023-10-01T12:00:00Z",
  "notes": "Server is currently down for maintenance."
}
```

##### **5.5. Delete History Entry**
- **Endpoint**: `DELETE /api/history/{id}/`
- **Response**:
```json
{
  "detail": "History entry deleted successfully."
}
```

### **Postman Collection**
برای ایجاد یک کالکشن در Postman، می‌توانید از این ساختار استفاده کنید. هر endpoint را به‌عنوان یک درخواست جدید اضافه کنید و اطلاعات مربوط به روش، URL و Body را پر کنید. همچنین می‌توانید توضیحات و مثال‌های پاسخ را به هر درخواست اضافه کنید تا مستندات شما کامل‌تر شود.

امیدوارم این داکیومنت و کالکشن به شما در استفاده از APIها کمک کند! اگر سوال دیگری دارید یا نیاز به اطلاعات بیشتری دارید، در خدمت شما هستم.