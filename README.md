We can write any number as the sequence of adding 1 and multiplying by 2:

     1 = 1
     2 = 1*2
     3 = 1*2+1
     4 = 1*2*2
     5 = 2*2+1
     6 = (2+1)*2
     7 = (2+1)*2+1
     8 = 2*2*2
     9 = 2*2*2+1
    10 = (2*2+1)*2
    11 = (2*2+1)*2+1
    12 = (2+1)*2*2
    13 = (2+1)*2*2+1
    14 = ((2+1)*2+1)*2
    15 = ((2+1)*2+1)*2+1

Now we don't really need (),+,-, because order is linear:

     1:1
     2:12
     3:121
     4:122
     5:1221
     6:1212
     7:12121
     8:1222
     9:12221
    10:12212
    11:122121
    12:12122
    13:121221
    14:121212
    15:1212121

In the canonic form of these numbers, noting that after 1, all numbers begin with 12, by shifting the indexing by 2, we can write these numbers in binary system (where 1 = 1 and 0 = 2):

     1:-----
     2:-----
     3:1
     4:0
     5:01
     6:10
     7:101
     8:00
     9:001
    10:010
    11:0101
    12:100
    13:1001
    14:1010
    15:10101

Noticing that 1 is never repeated twice, we can use 110 as a terminator, and then we can write such numbers one after another in juxtapostion, and decode them later without much fuzz. To translate such numbers into the usual form, only two operations are needed: bitwise shifting to the left (<<), and setting the lower bit of the register to 1 (bitwise or). 

--Nikita Sadkov
