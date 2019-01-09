# SVGCompiler
## But
Le but de ce projet était de générer des fichiers svg de façon dynamique à partir d'un langage source personnalisé
## Langages sources et objet choisis
### Langage source: personnalisé
#### Line break
```
instruction;
```

#### Shapes
```
[circle: radius=10, positionX=10 positionY=10, color=red;]
[triangle: width=10, height=20, positionX=10 positionY=10, color=blue;]
[rectangle: width=10, height=20, positionX=10 positionY=10, color=#FF00FF;]
```
- Implicit positionX : 0
- Implicit positionY : 0
- Implicit color : black
- Implicit radius : 1
- Implicit width : 1
- Implicit height : 1

#### Sementic

##### Type de variables
- boolean
- integer
- shape
```
boolean $my_bool = true;
integer $your_int = 42;
shape $their_circle = [circle: radius=10, positionX=3, positionY=4, color=red];
```

#### Draw
```
@ $shape
@ [circle: radius=10, positionX=10 positionY=10, color=red;]
```

#### Structures
##### If
```
if (cond)
{
	content;
}
elseif (cond2)
{
    content2;
}
else
{
    content3;
}
```

##### While
```
init;
while (cond)
{
	content;
	incr;
}
```

#### Comments
```
// comment
```

### Langage objet: SVG (un document entier est généré)
```html
<svg xmlns="http://www.w3.org/2000/svg">
<circle cx="15" cy="15" r="5" fill="#ff0000" />
<polygon points="15 20, 20 20, 17.5 15" fill="#0000ff"/>
<circle cx="30" cy="30" r="10" fill="#ff0000" />
<rect width="10" height="10" x="30" y="30" fill="#00ff00" />
<circle cx="60" cy="60" r="20" fill="#ff0000" />
<polygon points="60 80, 80 80, 70.0 60" fill="#0000ff"/>
<circle cx="120" cy="120" r="40" fill="#ff0000" />
<rect width="40" height="40" x="120" y="120" fill="#00ff00" />
<circle cx="240" cy="240" r="80" fill="#ff0000" />
<polygon points="240 320, 320 320, 280.0 240" fill="#0000ff"/>
<circle cx="480" cy="480" r="160" fill="#ff0000" />
<rect width="160" height="160" x="480" y="480" fill="#00ff00" />
<circle cx="960" cy="960" r="320" fill="#ff0000" />
<polygon points="960 1280, 1280 1280, 1120.0 960" fill="#0000ff"/>
<circle cx="1920" cy="1920" r="640" fill="#ff0000" />
<rect width="640" height="640" x="1920" y="1920" fill="#00ff00" />
</svg>
```

## Fonctionnalités implémentés

## Comment utiliser le compilateur
