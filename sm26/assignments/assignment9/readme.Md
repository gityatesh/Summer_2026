#  Technical Concepts & Algorithmic Problem Solving

This repository contains my reflections and solutions for various technical challenges spanning Algorithmic Optimization, Database Strategy (SQL), and Time/Space Complexity Analysis. 

Below is a breakdown of the core concepts and optimal solutions for each problem set.

---

##  Section A: Algorithmic Optimization

### 1. Revenue Pair Investigation (Two Sum)
* **Brute Force:** Using nested loops to check every possible pair results in a highly inefficient **O(n²)** time complexity.
* **Optimized Approach:** By utilizing a **Hash Set**, we can achieve an **O(n)** time complexity. As we iterate through the list, checking if the required complement exists in the Hash Set takes O(1) constant time. 
* **Trade-off:** While the time complexity drops significantly, the space complexity increases to **O(n)** to store the elements in the set.

### 2. Customer Record Cleanup (Handling Duplicates)
* **Brute Force:** Nested loops take **O(n²)** time.
* **Optimized Approach:** Because the input data is *already sorted*, we do not actually need an extra Hash Set. We can use a **Two-Pointer** technique to compare adjacent elements and overwrite duplicates in place.
* **Final Complexity:** Time: **O(n)** | Space: **O(1)**.

### 3. Merge Branch Reports
* **The Pitfall of `sort()`:** Appending two lists and using a built-in sort takes **O(n log n)** time, completely wasting the fact that the two lists are already sorted.
* **Optimized Approach:** Traverse both lists simultaneously using two pointers in a `while` loop. Compare the values at each pointer, append the smaller value to a new array, and move that specific pointer forward.
* **Final Complexity:** Time: **O(n)** | Space: **O(n)**.

### 4. Running Revenue Dashboard (Prefix Sums)
* **Concept:** Each position in the output array represents the cumulative sum of all previous values. 
* **Optimization:** By keeping a running total variable, we avoid recalculating the sum from scratch for every single index.
* **Final Complexity:** Time: **O(n)** | Space: **O(1)** (if modifying the original array in place).

### 5. Revenue Query System
* **Problem:** Running multiple queries (e.g., 10,000 times) using a standard loop takes **O(n * q)** time, which is too slow.
* **Solution:** We can precompute a Prefix Sum array. Setting up the array takes **O(n)** time upfront. Once built, answering *any* range query simply requires subtracting two indices: `PrefixSum[End] - PrefixSum[Start - 1]`.
* **Final Complexity:** Setup Time: **O(n)** | Query Time: **O(1)** | Space: **O(n)**.

---

##  Section B: Code Review & System Design

### 6. Code Review: Finding Duplicates
* **Original Code:** Relied on nested loops resulting in an **O(n²)** time complexity and lacked an early exit mechanism (it checked the whole list even after finding a duplicate).
* **Improved Code:** Implemented a Hash Set. The function immediately returns `True` the moment it finds a matching element, bringing the time complexity down to **O(n)** at the cost of **O(n)** space.

### 7. Modularity and Reusability
* **Concept:** Code should be written as independent, reusable services. 
* **Example:** A `get_customer_ranking` function from a customer service module can be easily imported and reused inside a `reward_service` to calculate coupons and cashback, preventing code duplication.

---

##  Section C: SQL & Database Strategy

### 8. Database Normalization (Customer Spending Report)
* **Why Two Tables?** Separating customer identity data (names) from transactional data (orders) ensures database normalization. It prevents redundant data entry and makes it easier to track individual customers who have multiple transactions.
* **Connection:** The tables are linked by declaring a `customer_id` in the transactions table as a **Foreign Key** that references the primary key (`id`) in the customers table.

### 9. Identifying Missing Data (Customers Without Orders)
* **INNER JOIN vs LEFT JOIN:** An `INNER JOIN` only returns intersecting data. A customer with zero orders would be completely dropped from the results. 
* **Solution:** A **LEFT JOIN** ensures all customers are listed. If a customer (e.g., Karan) has no transactions, the joined order columns will populate as `NULL`, allowing us to easily filter and identify them.

### 10. Comparing Against Global Metrics (High Value Customers)
* **Global Average:** The overall average spending is a single number calculated across *all* transactions in the database using the `AVG()` function. 
* **Query Strategy:** We first calculate an individual customer's total spending. Then, we use a `HAVING` clause paired with a Subquery `(SELECT AVG(amount) FROM transactions)` to filter out any customers whose personal total does not exceed the global average. 

---

##  Section D: Conceptual Reflection

* **O(n) vs O(n²):** **O(n)** represents linear time complexity—if the input size is 100, the code performs roughly 100 operations. **O(n²)** represents quadratic time complexity—an input size of 100 results in 10,000 operations, making it highly inefficient for large datasets.
* **The Importance of Data Structures:** The efficiency of an algorithm is heavily dependent on selecting the correct data structure. Using the wrong structure (like an Array instead of a Set for lookups) can drastically hinder performance.
* **Key Takeaway:** Understanding how to utilize Hash Tables and Dictionaries allows for highly optimized data storage and **O(1)** instant lookups, transforming complex nested loop problems into single-pass solutions.