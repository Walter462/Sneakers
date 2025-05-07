[TOC]

# Sneakers

This is an explainatory README for the educational problem project "Sneakers".
I try to develop the following skills:
- problem solving
- logical reasoning
- algorithmic thinking
- mathematical thinking
- computer science and software engineering

## Problem

Tom wants to buy a pair of new sneakers. He went to a nearby store and tried a few pairs by different brands. He picked a specific pair of sneakers that he liked. Considering the offline store price Tom decided to check if he could save some money by ordering them online. 

Tom found a few websites that sell the sneakers he picked. To decide which store to buy from he made the following table:

| Store   | Sneakers price, USD | Delivery fee, USD | Additional Conditions                         |
| ------- | ------------------- | ----------------- | --------------------------------------------- |
| Store 1 | $97.89$             | $3.16$            | Free delivery for cart sums over $105.26$ USD |
| Store 2 | $93.68$             | $5.26$            | None                                          |
| Store 3 | $105.26$            | $2.11$            | Discount of $10.53$ USD on the first order    |
| Store 4 | $100.00$            | Free              | None                                          |

## Reasoning

### Categorise the problem

Tom needs to decide which store to buy from. Assuming that the quality of the sneakers is the same, the `decision` problem is to choose the store with the lowest expenses (best `deal price`).

> Lets take a brief look at the table.

### Elements: extract
`descision`, `store list`, `store`, `deal price`

Tom's table represents a `stores list` helping to make a `decision` to pick a `store` based on the best `deal price`.

#### `decision`
The most important element of the problem is answer itself: a specific store, `descision` to be made.
#### `store list`

Second element is the store list to pick a store from. We can store lists inside computer memory using `python` for example.
##### `python list` small bite (skippable)
 Put comma "`,`" separated items in square "`[ ]`" brackets to create a list: `[item1, item2, item3 ]`.  Use equals `=` to assign a name to a list.
Use `print( )` to display a list.
`#` comment a line (execution ignore).


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
>TRY and PLAY online
[Click the red RUN button (top right) and feel free to change the code and play around](https://onecompiler.com/python/43gze9xnr)


####  `store`
`store list` consists of individual stores. It is the first Tom's table column.
#### `deal price`

The `descision` is based on the information about the `store` `deal price`. There is no such information as `deal price` in the Tom's table but we understand that the other 3 columns provide us with essential information related to the `deal price`:
- sneakers price
- delivery fee
- additional conditions

We can make `deal price` element more detailed by adding sub-elements to it but the main point here that no relevant information is lost. To keep it simple we avoid adding more known sub elements at this stage. Moreover the system  can increase in complexity. That means that Tom later can find some other factors impacting the deal price: (transaction fees, delivery insurance etc.). Having such abstraction as `deal price` can help us to handle this new information.

> [!important]
> `deal price` abstraction simplifies problem solving and potentially make the problem solving algorithm more flexible.

### Elements: relations
For now we got 4 elements:
 - `decision`
 - `store list`
 - `store`
 - `deal price`
Now lets take a closer look at elements combinatorics based on the common sense.
#### `decision` <--> `store list`
`descision` is a result of searching the lowest `deal price`  in the `store list`. 
Hence "searching the lowest `deal price`  in the `store list`" is the relation type between these 2 elements. To make it more abstract we can recognise that as searching minimum value in a list algoritm.

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

Fortunately `python` has a built-in function `min()`. It can take a list of numbers and return a minimal  value.
##### `python min()` small bite (skippable)
Print `min()` and put a list name inside round "`( )`" brackets: min(list_name).


Lets continue developing our [small python program](#-`python-list`-small-bite-(skippable)) and find out the cheapest sneakers price to depict the work of python `min()` function.


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
>This is NOT a `store` `deal price`! We excluded other important pricing factors such as delivery fee and store-specific conditions.

