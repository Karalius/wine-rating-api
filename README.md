# Wine rating API

## Purpose
....
## Rating
explain what 1-5 rating means

## Model

Link to jupyter notebook
Pipeline
Score

## POST
```json
curl -X POST https://wine-rating-api.herokuapp.com/predict -H 'Content-Type: application/json' -d
{
   "descriptions":[
      "Beverage Dynamics-Argentina- \"Floral and bright with big fruit that blasts out of the glass and is extremely approachable. Combining fresh raspberry and black currant notes, this a fun, punch, tannic cabernet that over-delivers.\"",
      "Jeb Dunnuck-Pessac-Leognan, Bordeaux, France- \"Deep ruby/purple, with stunning creme de cassis and blackberry fruits as well as kaleidoscope-like notes of graphite, scorched earth, smoke, violets, and spring flowers, it offers full-bodied richness yet stays light on its feet, graceful, and...\""
   ]
}
```
```json
{
   "Wine ratings":[
      2,
      5
   ]
}
```
## GET
```json
curl https://wine-rating-api.herokuapp.com/inferences
```
```json
[
   [
      24,
      {
         "descriptions":[
            "Wine Spectator-Willamette Valley, Oregon- \"Refined and stately in style, offering elegantly complex raspberry and cherry flavors, with orange peel and clove notes, gaining structure toward polished tannins.\""
         ]
      },
      {
         "Wine ratings":[
            2
         ]
      }
   ],
   [
      23,
      {
         "descriptions":[
            "Vinous-Tuscany, Italy - \"A stunning wine, the 2017 Ornellaia offers a captivating interplay of richness and energy...offers up an enticing melange of mocha, cedar, tobacco and licorice, with soft curves that add to its sensuality and allure. The 2017 is sumptuous and racy...\""
         ]
      },
      {
         "Wine ratings":[
            4
         ]
      }
   ],
   [
      22,
      {
         "descriptions":[
            "Jeb Dunnuck-Bolgheri, Tuscany, Italy- \"...offers serious intensity in its cassis, black cherry, graphite, bay leaf, forest floor, and spring flower aromas and flavors. Full-bodied and multi-dimensional on the palate, it has thrilling purity of fruit, ample tannins, and a great, great finish.\""
         ]
      },
      {
         "Wine ratings":[
            5
         ]
      }
   ],
   [
      21,
      {
         "descriptions":[
            "Wine Spectator-Pomerol, Bordeaux, France- \"A sleeping giant. Dark ruby in color, showing aromas of blackberry, and green olive, with a hint of mineral. Full-bodied, with ultrafine tannins and a supercaressing mouthfeel. Coffee, dark chocolate and berry. Chewy yet balanced. Very long in the mouth.\""
         ]
      },
      {
         "Wine ratings":[
            2
         ]
      }
   ],
   [
      20,
      {
         "descriptions":[
            "James Suckling-Napa Valley, California - \"Lots of blackberries and wet earth with mahogany and spice. Full-bodied, tight and composed with long, silky tannins. Shows length and depth...already beautiful.\""
         ]
      },
      {
         "Wine ratings":[
            3
         ]
      }
   ],
   [
      19,
      {
         "descriptions":[
            "James Suckling-Pessac, Bordeaux, France - \"Rose petals, sandalwood and currants with some plums and fruit tea. Full-bodied, tight and focused. Incredibly straight and minerally. Toned muscles here. Tannic. Traditional and unwavering.\""
         ]
      },
      {
         "Wine ratings":[
            5
         ]
      }
   ],
   [
      18,
      {
         "descriptions":[
            "Wine Enthusiast -2nd Growth, Pauillac, Bordeaux, France-\"This great estate in southern Pauillac, facing the Latour vineyard, is at the top of its game. In this release, the tannins are as impressive and dense as the black fruits. Together they form a harmonious ensemble, richly structured,...\""
         ]
      },
      {
         "Wine ratings":[
            5
         ]
      }
   ],
   [
      17,
      {
         "descriptions":[
            "Wine Spectator-St. Emilion, Bordeaux, France- \"This offers a lovely display of boysenberry, cherry and plum fruit, yet stays refined and focused, relying on purity as this glides through. Has weight but feels silky, with a flinty mineral hint adding cut on the finish..\""
         ]
      },
      {
         "Wine ratings":[
            5
         ]
      }
   ],
   [
      16,
      {
         "descriptions":[
            "Jeb Dunnuck-Pessac-Leognan, Bordeaux, France- \"Deep ruby/purple, with stunning creme de cassis and blackberry fruits as well as kaleidoscope-like notes of graphite, scorched earth, smoke, violets, and spring flowers, it offers full-bodied richness yet stays light on its feet, graceful, and...\""
         ]
      },
      {
         "Wine ratings":[
            5
         ]
      }
   ],
   [
      15,
      {
         "descriptions":[
            "Beverage Dynamics-Argentina- \"Floral and bright with big fruit that blasts out of the glass and is extremely approachable. Combining fresh raspberry and black currant notes, this a fun, punch, tannic cabernet that over-delivers.\""
         ]
      },
      {
         "Wine ratings":[
            2
         ]
      }
   ]
]
```
## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
