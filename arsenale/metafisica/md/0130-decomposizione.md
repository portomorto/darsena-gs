---
title: "decomposizione e scoperta del movimento"
layout: page
parent: "Premessa Epistemologica"
nav_order: 3
last_modified_date: 2025-02-04 12:26:00 CET
---

## l'unità apparente

Il modello matematico dell'unità è piuttosto immediato: l'uno. Non ne
vogliamo solo la sua integrità naturale, ma ne vogliamo anche la sua
granularità elementare che ci permette di vederlo con un doppio senso:

 - l'unità come integrità, solidità (naturale);
 - l'unità come passo, grano, elemento minimo del movimento e delle sue
 osservazioni.

Iniziamo con la rappresentazione dell'unità come segnale numerico,
un segnale digitale che ha rappresentazione costante:

```c++
import("stdfaust.lib");
process = 1;
```

Il circuito disegnato con Faust ci presenta alla sua uscita un segnale
con ampiezza costante:

$$y(t)=1$$

appunto, uno.

Sia $U = \{1\}$ l'insieme singoletto che rappresenta l'unità apparente dell'oggetto.

> Tuttavia, nessuna “leggitimità” può cancellare quell'originario tratto
  _impositivo_ del potere di Polemos per cui essa fa si che i distinti siano,
  ek-sistano, per cui esso impone loro i confini in base ai quali si oppongono.
  Come fondare questa originaria _violenza?_ Essa appare come fondamento in
  nessun modo a sua volta fondabile, _s-fondo_ di ogni ulteriore discorso;
  _Anánke_, necessario così accada, pre-potente rispetto alla stessa potenza di
  Polemos; Polemos infatti opera soltanto in base al pre-potente Principio per
  cui _mostrare, produrre, manifestare_ non possono significare se non che i
  _distinti-opposti_ esistono e che all'uno è proibito essere l'altro. [p.26]

## la sottrazione del movimento: verso la decomposizione

Uno modo piuttosto semplice per convincersi della necessità (agonistica)
di decomposizione e ricomposizione, e composizione, viene
dall'osservazione della relazione tra l'uno, unitario, e un oggetto in
movimento. La relazione può essere costruttiva e distruttiva e solo per
semplificazione scegliamo quella distruttiva: sottraiamo all'uno
un oggetto in movimento, un'oscillazione, un'onda.

Definiamo una funzione d'onda

$$w(t): \mathbb{R} \to [0,1]$$

tale che:

$$w(t) = \frac{1}{2}(\sin(\omega t) + 0.5)$$

dove $\omega$ rappresenta la frequenza angolare (nel nostro esempio, $\omega = 2\pi \cdot 1000$).

Procediamo con la sottrazione dall'uno di una componente oscillatoria a
frequenza conosciuta (es. 1000Hz):

```c++
import("stdfaust.lib");
// definizione dell'oscillazione unipolare tra 0 e 1
wave = os.osc(1000)/2+0.5;
process = 1-wave;
```

Osserviamo, con un certo stupore che quell'unità apparente iniziale,
in relazione (interferenza) con un segnale in movimento produce un
movimento altro, un altro movimento, arriverei a supporre:
un movimento complementare.

L'operazione di sottrazione può essere formalizzata come:

$$f(t) = 1 - w(t)$$

La ricomposizione dell'unità si esprime come:

$$w(t) + f(t) = w(t) + (1 - w(t)) = 1$$

## La Ricomposizione dell'Unità e la composizione dell'uno.

Concediamoci il dubbio: ma se volessi ricomporre l'uno iniziale, statico,
integro e solido, potrei farlo quindi con due oggetti in movimento in
relazione? Si, mostriamo infine la ricomposizione dell'unità:

```c++
import("stdfaust.lib");
wave = os.osc(1000)/2+0.5;
process = 1-wave+wave;
```

Il gioco è fatto, d'ora in poi potrete decidere se osservare l'uno come
monolite, statico, o come emersione di relazioni, come soglia verso
una comoplessità da decomporre, ricomporre e, opportunamente, comporre:
a definire da quale parte siete è il vostro tasso di agonia.

## Generalizzazione

Questo modello può essere esteso considerando uno spazio vettoriale $V$
su $\mathbb{R}$, dove ogni elemento rappresenta una possibile
“componente dinamica” dell'unità apparente. In questo contesto,
l'unità può essere vista come un punto fisso sotto determinate
trasformazioni.
