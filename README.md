# Illustrated Prejudice

This is a fun project inspired by Parable of the Polygons. (You can find it here -> https://ncase.me/polygons/)

It illustrates how small individual prejudices how ever small add up to drastic societal prejudice.

![](/images/default.png)

Read the post about Parable of the polygons and try to complete the challenge below.

![](/images/with_bias.png)

Try and get the segregation percent as low as possible by setting the condition where a shape wants to move.

```
▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ □     ▼     □ ▼ ▼ □ ▼ ▼
  ▼ □ □ □ ▼ □ □ □ □ ▼     ▼ □ □ □ ▼ ▼ ▼
□ ▼ □ ▼ ▼ □ ▼ ▼ □ □ ▼ ▼ ▼ ▼ ▼ □ ▼ ▼ ▼ □
□ ▼ □ □ ▼ □ □ ▼   ▼ □ □ □ □ ▼ ▼ ▼ □ □ □
▼ ▼ □ □ ▼ ▼ □ □ ▼ □ □ □ □ □ □ □ ▼ ▼ □  
▼ □ ▼   ▼ □ □   □ ▼ ▼ ▼ ▼ □ □ ▼ ▼ ▼   □
▼ ▼ □ ▼ ▼ □ □ □   ▼ □ ▼ ▼ ▼ □ ▼     ▼ □
  ▼ □ ▼ □   □     □ □ □ □ ▼ ▼ □ ▼   ▼ ▼
  ▼ ▼ □ □ □ □   □ □     □ □ □ □ ▼ ▼ ▼  
  ▼ □ ▼ ▼ ▼ □ □ □ □ □ ▼ □   □ ▼ ▼ ▼   ▼
▼   ▼ □ □ ▼   □ ▼ ▼ ▼ ▼   ▼   ▼ ▼ ▼ ▼ ▼
▼ ▼ □ □ ▼   ▼ ▼     ▼ ▼ ▼ ▼   ▼ ▼ □ ▼ □
▼   ▼ ▼ ▼ ▼   ▼ ▼ ▼ ▼ ▼ □ □ ▼ ▼ □ □ □ □
▼ ▼ ▼ ▼ □ ▼ ▼ □   ▼ ▼ ▼ □ ▼ ▼ ▼ □ ▼ ▼ ▼
  ▼ □ □ □ ▼ ▼ □ □ □   ▼ □ □ □ □ ▼   ▼ ▼
  □ □ □ □ □ ▼ ▼ ▼ ▼ □ ▼ □ □ □ □ ▼ ▼ ▼  
□   □ □ □ ▼ □ □ □ ▼ □   ▼ ▼ □ ▼ □ □ □ □
□ ▼ □   □ □ ▼ □ ▼ □ ▼ □ □ □ ▼ ▼ □ □ □  
▼ ▼ ▼ □ □ □ ▼ ▼ □ □ □ ▼ □ □ ▼ ▼   □ □ □
□ □ ▼ ▼ □ ▼ ▼ ▼ □   □ ▼ ▼ ▼ □ ▼ □ □   □
Segregated: 54%

We have reached 100% happiness

Where Shapes want to move if this is not True:
<like-neighbor-percentage> >= 1/3
```

Edit the `happiness_condition` variable at the bottom of main.py
Then run main.py with `python main.py` or in your IDE

Have fun!