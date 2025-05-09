# 1. Sneakers

This is a  README for the educational problem project "Sneakers".
I am still learning and focus on develop the following skills:
- problem solving
- logical reasoning
- algorithmic thinking
- mathematical thinking
- computer science and software engineering

If you are interested please join my reasoning logic and feel free to criticize it.

## 2. Problem

Tom wants to buy a pair of new sneakers. He went to a nearby store and tried a few pairs of different brands. He picked a specific pair of sneakers that he liked. Considering the offline store price Tom decided to check if he could save some money by ordering them online. 

Tom found a few websites that sell the sneakers he picked. To decide which store to buy from he made the following table:

| Store   | Sneakers price, USD | Delivery fee, USD | Additional Conditions                         |
| ------- | ------------------- | ----------------- | --------------------------------------------- |
| Store 1 | $97.89$             | $3.16$            | Free delivery for cart sums over $105.26$ USD |
| Store 2 | $93.68$             | $5.26$            | None                                          |
| Store 3 | $105.26$            | $2.11$            | Discount of $10.53$ USD on the first order    |
| Store 4 | $100.00$            | Free              | None                                          |


## 3. Categorise the problem

Tom needs to decide which store to buy from. Assuming that the quality of the sneakers is the same, the `decision` problem is to choose the store with the lowest expenses (best `deal price`).

Lets take a brief look at the table.

---

## 4. Elements: extract
`descision`, `store list`, `store`, `deal price`


Tom's table represents a `store list` helping to make a `decision` to pick a `store` based on the best `deal price`.

---

### 4.1. `decision`


The most important element of the problem is answer itself: a specific store, `descision` to be made.

---

### 4.2. `store list`

Second element is the store list to pick a store from. 

>[!tip] 
`python list` small bite (skippable section).
We can store lists inside computer memory using `python` programming language.
Put comma "`,`" separated items in square "`[ ]`" brackets to create a list: `[item1, item2, item3 ]`.  Use equals `=` to assign a name to a list.
Use `print( )` to display a list. `#` comment a line (execution ignore).

```python
# create sneakers price list and assign it to a variable `sneakers_price_list`
sneakers_price_list = [97.89, 93.68, 105.26, 100.00]
# print on display sneakers_price_list
print(sneakers_price_list)
```
result:
```
[97.89, 93.68, 105.26, 100.00]
```

>[!tip]
>TRY and PLAY online [Click the red RUN button (top right) and feel free to change the code and play around](https://onecompiler.com/python/43gze9xnr)

---

### 4.3. `store`
Store list consists of individual stores. It is the first Tom's table column.

---

### 4.4. `deal price`
The `descision` is based on the information about the `store` `deal price`. There is no such information as `deal price` in the Tom's table but we understand that the other 3 columns provide us with essential information related to the `deal price`:
- sneakers price
- delivery fee
- additional conditions

We can make `deal price` element more detailed by adding sub-elements to it but the main point here that no relevant information is lost. To keep it simple we avoid adding more known sub elements at this stage. Moreover the system  can increase in complexity. That means that Tom later can find some other factors impacting the deal price: (transaction fees, delivery insurance etc.). Having such abstraction as `deal price` can help us to handle this new information.

To sum up, we can say that we united 3 columns into one abstraction: **`deal price`**.  
The Tom's table could look something like this:

<table>
  <thead>
    <tr>
      <th rowspan="2">Store</th>
      <th colspan="3">Deal price, USD</th>
    </tr>
    <tr>
      <th>Sneakers price, USD</th>
      <th>Delivery fee, USD</th>
      <th>Additional Conditions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Store 1</td>
      <td>$97.89</td>
      <td>$3.16</td>
      <td>Free delivery for cart sums over $105.26 USD</td>
    </tr>
    <tr>
      <td>Store 2</td>
      <td>$93.68</td>
      <td>$5.26</td>
      <td>None</td>
    </tr>
    <tr>
      <td>Store 3</td>
      <td>$105.26</td>
      <td>$2.11</td>
      <td>Discount of $10.53 USD on the first order</td>
    </tr>
    <tr>
      <td>Store 4</td>
      <td>$100.00</td>
      <td>Free</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

> [!important] 
> The `deal price` abstraction simplifies problem solving and can potentially make the algorithm more flexible. Later we can add other `deal price` sub-elements if needed (like transaction fees, delivery insurance etc.).

--- 

## 5. Elements: relations
For now we got 4 elements:
 - `decision`
 - `store list`
 - `store`
 - `deal price`
  
Now lets take a closer look at elements combinatorics based on the common sense.

---

### 5.1. `decision` <--> `store list`
`descision` is a result of searching the lowest `deal price`  in the `store list`. 
Hence "searching the lowest `deal price`  in the `store list`" is the relation type between these 2 elements. We recognise that as searching minimum value in a list algoritm.

Output (algorithm returns a value): `descision`
Algorithm (apply to input): find minimum
Input (algorithms gets a data to work on): `store list`

>[!note]
>Finding list minimum data flow diagram:
>```mermaid
>%%{ init : { "themeVariables": { "htmlLabels": true }}}%%
>graph LR
>	in@{label: "Input: \n <code>list=[item1, item2, item3]</code>"}
>	fn@{shape: diamond, label: "Find mininum value\n algorithm:\n <code>min(list)</code>"}
>	out@{label: "Output: \n <code>item</code> "}
>	in --- fn --- out
>```

---

>[!tip] 
`python list` small bite (skippable section)
Fortunately `python` has a built-in function `min()`. It can take a list of numbers and return a minimal  value. Put a list name inside round "`( )`" brackets of `min()`: `min(list_name)`.

[small python program](#-store-list)


```python
# 1. INPUT data
# create sneakers price list and assign it to a variable `sneakers_price_list`
sneakers_price_list = [97.89, 93.68, 105.26, 100.00]
# print on display sneakers_price_list
print(f"The sneakers price list: {sneakers_price_list}")

# 2. ALGORITHM application
# apply min() to `sneakers_price_list` and assign the result to a variable `minimal_sneakers_price`
minimal_sneakers_price = min(sneakers_price_list)

# 3. OUTPUT data (applied algorithm result)
# print  minimal_sneakers_price
print(f"Minimal price is: {minimal_sneakers_price}")
```
result:
```
The sneakers price list: [97.89, 93.68, 105.26, 100.0]
Minimal price is: 93.68
```

>[!tip]
>TRY and PLAY online
[Click the red RUN button (top right) and feel free to change the code and play around](https://onecompiler.com/python/43gzn7zvr)


>[!CAUTION]
[table above](#-deal-price)
 

---
