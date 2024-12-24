# Xush kelibsiz
# Listlar bo‘yicha bo‘laklash (Slicing List)

Uy vazifalari va test topshiriqlarini avtomatlashtirilgan tekshirish
- ushbu repozitoriyani fork qiling
- topshiriqni bajaring
- to'g'ri xabar bilan commit qiling

# Muammolar
## Slicing_list01

  **Numbers** nomli ro‘yxat berilgan. Juft indeksdagi elementlarni qaytaring.

**Misol 1:**

```Python
Input: list1=[1, 2, 3, 4, 5]
Output: [1,3,5]

```

**Misol 2:**

```Python
Input: list1=[0, 1, 2, 3, 4, 5]
Output: [0, 2, 4]

```
**Cheklovlar:**

  - 2 <= length(list1) <= 10^5

## Slicing_list02

  Bir nechta elementlardan iborat ro‘yxat berilgan. Ushbu ro‘yxatni teskari tartibda qaytaring.

**Misol 1:**

```Python
Input: list1=[1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

```

**Misol 2:**

```Python
Input: list1=[0, 1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1, 0]

```
**Cheklovlar:**

  - 2 <= length(list1) <= 10^5

## Slicing_list03

  Bir nechta elementlardan iborat ro‘yxat berilgan. Ushbu ro‘yxatni o‘zining teskari versiyasi bilan birlashtirib qaytaring.

**Misol 1:**

```Python
Input: list1=['a', 'b', 'c', 'd']
Output: ['a', 'b', 'c', 'd', 'd', 'c', 'b', 'a']

```

**Misol 2:**

```Python
Input: list1=[0, 1, 2]
Output: [0, 1, 2, 2, 1, 0]

```
**Cheklovlar:**

  - 2 <= length(list1) <= 10^5

## Slicing_list04

  Bir nechta elementlardan iborat ro‘yxat berilgan. Boshlanishdan uchta elementni qaytaring.

**Misol 1:**

```Python
Input: list1=['a', 'b', 'c', 'd']
Output: ['a', 'b', 'c']

```

**Misol 2:**

```Python
Input: list1=['a', 1, 'b', 2, 'c', 3, 'd', 4]
Output: ['a', 1, 'b']

```
**Cheklovlar:**

  - 4 <= length(list1) <= 10^5

## Slicing_list05

  Bir nechta elementlardan iborat ro‘yxat berilgan. n-indeksdan k-indeksgacha bo‘lgan elementlarni qaytaring.

**Misol 1:**

```Python
Input: list1=['a', 'b', 'c', 'd', 'e', 'f'] n = 2 k = 5
Output: ['c', 'd', 'e']

```

**Misol 2:**

```Python
Input: list1=['a', 1, 'b', 2, 'c', 3, 'd', 4] n = 1 k = 3
Output: [1, 'b']

```
**Cheklovlar:**

  - 4 <= length(list1) <= 10^5
  - 1 <= n <= k <= length(list1)

## Slicing_list06

  Bir nechta elementlardan iborat ro‘yxat berilgan. Boshlanishdan har uchinchi elementni qaytaring.

**Misol 1:**

```Python
Input: list1=['a', 'b', 'c', 'd', 'e', 'f']
Output: ['a', 'd']

```

**Misol 2:**

```Python
Input: list1=['a', 1, 'b', 2, 'c', 3, 'd', 4]
Output: ['a', 2, 'd']

```
**Cheklovlar:**

  - 4 <= length(list1) <= 10^5

## Slicing_list07

  Bir nechta elementlardan iborat ro‘yxat berilgan. Boshlanishdan n qadamli barcha elementlarni qaytaring.

**Misol 1:**

```Python
Input: list1=['a', 'b', 'c', 'd', 'e', 'f'] n = -1
Output: ['f', 'e', 'd', 'c', 'b', 'a']

```

**Misol 2:**

```Python
Input: list1=['a', 1, 'b', 2, 'c', 3, 'd', 4] n = 2
Output: ['a', 'b', 'c', 'd']

```
**Cheklovlar:**

  - 4 <= length(list1) <= 10^5
  - -1 <= n < length(list1)


## Slicing_list08

  Bir nechta elementlardan iborat ro‘yxat berilgan. Tugashdan n qadamli barcha elementlarni qaytaring.

**Misol 1:**

```Python
Input: list1=['a', 'b', 'c', 'd', 'e', 'f'] n = -1
Output: ['a', 'b', 'c', 'd', 'e', 'f']

```

**Misol 2:**

```Python
Input: list1=['a', 1, 'b', 2, 'c', 3, 'd', 4] n = 2
Output: [4, 3, 2, 1]

```
**Cheklovlar:**

  - 4 <= length(list1) <= 10^5
  - -1 <= n <= length(list1)

## Slicing_list09

  Bir nechta elementlardan iborat ro‘yxat berilgan. Boshlanishdan n elementdan tashqari hammasini qaytaring.

**Misol 1:**

```Python
Input: list1=['a', 'b', 'c', 'd', 'e', 'f'] n = 3
Output: ['d', 'e', 'f']

```

**Misol 2:**

```Python
Input: list1=['a', 1, 'b', 2, 'c', 3, 'd', 4] n = 2
Output: ['b', 2, 'c', 3, 'd', 4]

```
**Cheklovlar:**

  - 4 <= length(list1) <= 10^5
  - -1 <= n <= length(list1)

## Slicing_list10

  Bir nechta elementlardan iborat ro‘yxat berilgan. Boshlanishdan n elementdan tashqari hammasini teskari tartibda qaytaring.

**Misol 1:**

```Python
Input: list1=['a', 'b', 'c', 'd', 'e', 'f'] n = 3
Output: ['f', 'e', 'd']

```

**Misol 2:**

```Python
Input: list1=['a', 1, 'b', 2, 'c', 3, 'd', 4] n = 2
Output: [4, 'd', 3, 'c', 2, 'b']

```
**Cheklovlar:**

  - 4 <= length(list1) <= 10^5
  - -1 <= n <= length(list1)

# Ogohlantirish
- boshqa yechimlarni yoki har qanday yechimni ko‘chirmang
- sharhlarni o‘chirmang
