# Selection Sort - Chapter 2

## Learning Goals

- Learn about **arrays** and **linked lists**
- Be able to explain the tradeoffs between arrays and linked lists
- Be able to sort your list using **selection sort**

## How does memory work?

![](images/2021-01-22-07-06-00.png)

Your computer memory is like a "chest of drawers". When you have items to store, the computer will assign you some drawers to leave things in.

![](images/2021-01-22-07-06-10.png)

Each of the drawers has an address.

![](images/2021-01-22-07-06-27.png)

What's the general process for storing items?

1. Get some space in the memory
2. Get the address to this space
3. Use either an array or list to store the items

## Arrays and linked lists

How are arrays stored in memory?

- The items in an array are stored **contiguously**, i.e. right next to each other in the memory space.

What happens if there isn't enough allocated space to store everything next to each other?

- You have to ask the computer for another memory spot.

![](images/2021-01-22-07-10-23.png)

- Every time the array fills up, a new array has to be initialized to store more items.

What's the alternative to creating a new array each time you want to add an extra item?

- Make a bigger array, e.g. 10 spots for 10 items instead of 3 items. That way, when you want to add more items, you can use the same array.
- What's the problem of making a bigger array?
  - The empty spots are wasted until you use them. It's like reserving seats in a restaurant. Having a 10-seat round table is great when you have a lot of guests. But if you are only eating with one other person, then that's 8 seats you've wasted. It's even more costly if there is a mandatory gratuity and you're charged tips for 10 people instead of tips for 2 people. That's what it's like with arrays: Making bigger arrays lets you store more items, but the extra storage comes at a cost.
  - You might still have to make a bigger array you add more than 10 items!

### Linked Lists

How do linked lists solve the problem of adding items to full lists?

- Instead of requiring items to be next to each other, linked lists allow you to store items anywhere in memory. That way, you don't have to relocate the entire list and there isn't exactly a set maximum for how many items you can store.

![](images/2021-01-23-06-48-14.png)

How do linked lists work then?

- When you store an item in a linked list, you store it in a memory location and also store a pointer to the next item in the linked list.

What are the downsides of linked lists?

- You have to view items one at a time because items can be stored anywhere in memory and you only know where a particular item is based on the pointer in the previous item (in a singly-linked list).

- By contrast, arrays are useful for **random access**, i.e. viewing any item in the list because it's easy to tell where an item is located.

![](images/2021-01-23-06-52-03.png)

### Why does it take O(n) time to insert an element into an array? Suppose you want to insert an element at the beginning of an array? How would you do it? How long would it take?

O(n) time means that in the worst case, it takes about n steps to insert an element into an array. When you insert an element into the last available spot in an array, you don't have to move any other element, so it takes O(1) time. However, if there is already a value in that spot, then you have to move that value over to the right by one. For each extra index that's already full, n, the number of steps taken grows by n factors, so that's O(n).

Suppose you have an array with 5 spots: `_ _ _ _ _`.

1. Insert an element, 1, into index 0 (the first spot) takes constant time because there isn't anything there: `1 _ _ _ _`
2. Inserting an element, 2, into index 0 takes an extra step because there is already a value in index 0. First, move the 1 to index 1 to make space:
   1. `_ 1 _ _ _`. Now, you can insert 2.
   2. `2 1 _ _ _`. That took an extra step.
3. Inserting another element, 3, into index 0 take yet another step because now you have to move elements 2 and 1.
   1. `2 _ 1 _ _ ` First, move 1 so that 2 can be moved over.
   2. `_ 2 1 _ _ ` Second, move 2 over to the right so 3 can fit.
   3. `3 2 1 _ _ ` Now you can insert 3.

### Exercise

> 2.1 Suppose you’re building an app to keep track of your finances.
> Every day, you write down everything you spent money on. At the end of the month, you review your expenses and sum up how much you spent. So, you have lots of inserts and a few reads. Should you use an array or a list?

Since there are few reads, then random access shouldn't be an issue, so that's one less reason to use an array.

The next thing to consider is _where_ you want to be able to insert the items. If it's into any particular spot, then it'll take O(n) time for insertion using an array or O(1) for a linked list. However, if it's at the end of the list sequentially, then it'll be O(1) time for both linked lists and arrays. I'll assume that you want to be able to organize the list, to make things easier for you to keep track of. Sorting involves insertion, deletions, etc, which takae O(N) time in arrays. Therefore, I'd recommend linked lists so you can insert items wherever you want.

### Inserting into the middle of the list

If you want to order the list, it's easier to do so with the linked lists instead of arrays. Just change what the previous element points to:
![](images/2021-01-23-07-16-00.png)

With arrays, you have to move items down:
![](images/2021-01-23-07-16-28.png)

### Deletions?

Lists are better here too. Lists beat arrays in insertions and deletions (assuming you have access to them), but arrays beat lists in random access (read data)

![](images/2021-01-23-07-17-16.png)

What is **random access**?

- Being able to get the value of any element in the list

What is **sequential access**?

- Getting the values of elements in a list one by one, from beginning to end.

### Exercises 2.2-2.5

> 2.2 Suppose you’re building an app for restaurants to take customer orders. Your app needs to store a list of orders. Servers keep adding orders to this list, and chefs take orders of the list and make them. It’s an order queue: servers add orders to the back of the queue, and
> the chef takes the first order of the queue and cooks it.
> Would you use an array or a linked list to implement this queue? (Hint: Linked lists are good for inserts/deletes, and arrays are good for random access. Which one are you going to be doing here?)

It seems that the cook is just cooking things in the order they receive them. That takes O(1) time to look at the first item and cook it. Both arrays and linked lists provide easy access to the first item. Therefore, it doesn't really matter whether you use linked lists or arrays for looking up the first item. The thing is that you don't know how many orders will come in, so the array might get filled up and you waste time trying to make a new array. Instead, I'd use a linked list because you can keep adding items to the end of it.

> 2.3 Let’s run a thought experiment. Suppose Facebook keeps a list of usernames. When someone tries to log in to Facebook, a search is done for their username. If their name is in the list of usernames, they can log in. People log in to Facebook pretty oten, so there are
> a lot of searches through this list of usernames. Suppose Facebook uses binary search to search the list. Binary search needs random access—you need to be able to get to the middle of the list of usernames instantly. Knowing this, would you implement the list as an array or a linked list?

Array, which supports random access. Binary search requires being able to access the middle of the list immediately instead of sequentially accessing items one by one. Linked lists would require looking at each item one by one which would be way too slow.

> 2.4 People sign up for Facebook pretty oten, too. Suppose you decided to use an array to store the list of users. What are the downsides of an array for inserts? In particular, suppose you’re using binary search to search for logins. What happens when you add new users to an array?

Insertions and deletions have a runtime of O(n). When you use a binary search for logins, you have to keep the array sorted. That means there's a good chance you'll be inserting items into the middle of the list, which would be O(n) time... which would take a while.

> 2.5. In reality, Facebook uses neither an array nor a linked list to store user information. Let’s consider a hybrid data structure: an array of linked lists. You have an array with 26 slots. Each slot points to a linked list. For example, the first slot in the array points to a linked list containing all the usernames starting with a. The second slot points to a linked list containing all the usernames starting with b, and so on.

    ![](images/2021-01-23-07-26-32.png)

> Suppose Adit B signs up for Facebook, and you want to add them to the list. You go to slot 1 in the array, go to the linked list for slot 1, and add Adit B at the end. Now, suppose you want to search for Zakhir H. You go to slot 26, which points to a linked list of all the Z names. hen you search through that list to ind Zakhir H.
> Compare this hybrid data structure to arrays and linked lists. Is it slower or faster than each for searching and inserting? You don’t have to give Big O run times, just whether the new data structure would be faster or slower.

This hybrid data structure would be faster than arrays for insertions and deletions because you'd quickly find the linked list it is in and then take advantage of the linked list O(1) insertion/deletion run time. However, for searching it'd be slower than the array because you'd have to sequentially access names in the 'Z' linked list.

## Selection sort


## Ankified Recap

**Simple Data Structure**: With an {{c1::array}}, all the elements are stored {{c2::next}} to each other in memory.

- ![](images/2021-01-23-07-33-37.png)

**Simple Data Structure**: With a {{c1::linked list}}, elements are stored in {{c2::different}} spots in memory.

- ![](images/2021-01-23-07-36-01.png)

**Arrays** allow {{c1::fast / O(1)}} {{c2::reads / random access}}.

**Linked lists** allow {{c3::fast O(1)} {{c1::inserts}} and {{c2::deletes}}.

- Extra: Assuming you have the relevant pointers.
