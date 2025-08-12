# 🍽️ Local Food Wastage Management System

## 📌 Overview
The **Local Food Wastage Management System** is a data-driven solution designed to connect **food providers** (restaurants, supermarkets, grocery stores, etc.) with **receivers** (NGOs, shelters, individuals).  
The goal is to **reduce food wastage** by efficiently managing surplus food and matching it with demand.

This project combines:
- **Python & Pandas** for data processing
- **SQLite** for database storage and querying
- **Streamlit** for a user-friendly web interface

---

## 📂 Dataset Description
We work with **four datasets**, each containing 1000 rows:

1. **`providers.csv`**
   - `Provider_ID`
   - `Name`
   - `Type` (Supermarket, Grocery Store, Restaurant, Catering Service)
   - `Address`
   - `City`
   - `Contact`

2. **`receivers.csv`**
   - `Receiver_ID`
   - `Name`
   - `Type` (NGO, Individual, Shelter)
   - `City`
   - `Contact`

3. **`food_listings.csv`**
   - `Food_ID`
   - `Food_Name`
   - `Quantity`
   - `Expiry_Date`
   - `Provider_ID`
   - `Provider_Type`
   - `Location` (City)
   - `Food_Type` (Vegetarian, Non-Vegetarian, Vegan)
   - `Meal_Type` (Breakfast, Lunch, Dinner, Snacks)

4. **`claims.csv`**
   - `Claim_ID`
   - `Food_ID`
   - `Receiver_ID`
   - `Status` (Pending, Completed, Cancelled)
   - `Timestamp`

---

## ⚙️ Project Workflow
### **Step 1 – Data Loading**
- Load the CSV files into Pandas DataFrames.
- Display basic info: shape, column names, and sample rows.

### **Step 2 – Create SQLite Database**
- Create a local database in Colab.
- Use `to_sql()` to save each DataFrame as a table.
- Verify table creation.

### **Step 3 – SQL Queries**
Some example queries implemented:
1. **Count providers and receivers per city**
2. **Top provider type by total food quantity**
3. **Providers with pending claims**
4. **Top 10 most claimed food items**
5. **Total available vs claimed quantities**

### **Step 4 – Streamlit App**
- A web-based interface to:
  - View providers, receivers, food listings, claims
  - Run custom SQL queries
  - View query results instantly

---

## 💡 Example SQL Queries
```sql
-- Provider type with most quantity
SELECT Provider_Type, SUM(Quantity) AS total_quantity
FROM food_listings
GROUP BY Provider_Type
ORDER BY total_quantity DESC;

-- Top 10 claimed foods
SELECT f.Food_Name, COUNT(c.Claim_ID) AS total_claims
FROM claims c
JOIN food_listings f ON c.Food_ID = f.Food_ID
GROUP BY f.Food_Name
ORDER BY total_claims DESC
LIMIT 10;
