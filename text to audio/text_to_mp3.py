from gtts import gTTS
from mpyg321.mpyg321 import MPyg321Player

text = '''1-3 Atomic processes
WATER EVAPORATING IN AIR
OXYGEN HYDROGEN NITROGEN
Figure 1-5
So much for the description of solids, liquids, and gases from the atomic point
of view. However, the atomic hypothesis also describes processes, and so we shall
now look at a number of processes from an atomic standpoint. The first process
that we shall look at is associated with the surface of the water. What happens at
the surface of the water? We shall now make the picture more complicated—and
more realistic—by imagining that the surface is in air. Figure 1-5 shows the
surface of water in air. We see the water molecules as before, forming a body of
liquid water, but now we also see the surface of the water. Above the surface
we find a number of things: First of all there are water molecules, as in steam.
This is water vapor, which is always found above liquid water. (There is an
equilibrium between the steam vapor and the water which will be described later.)
In addition we find some other molecules—here two oxygen atoms stuck together
by themselves, forming an oxygen molecule, there two nitrogen atoms also stuck
together to make a nitrogen molecule. Air consists almost entirely of nitrogen,
oxygen, some water vapor, and lesser amounts of carbon dioxide, argon, and
other things. So above the water surface is the air, a gas, containing some water
vapor. Now what is happening in this picture? The molecules in the water are
always jiggling around. From time to time, one on the surface happens to be hit a
little harder than usual, and gets knocked away. It is hard to see that happening
in the picture because it is a still picture. But we can imagine that one molecule
near the surface has just been hit and is flying out, or perhaps another one has
been hit and is flying out. Thus, molecule by molecule, the water disappears—it
evaporates. But if we close the vessel above, after a while we shall find a large
number of molecules of water amongst the air molecules. From time to time, one
of these vapor molecules comes flying down to the water and gets stuck again.
So we see that what looks like a dead, uninteresting thing—a glass of water with
a cover, that has been sitting there for perhaps twenty years—really contains
a dynamic and interesting phenomenon which is going on all the time. To our
eyes, our crude eyes, nothing is changing, but if we could see it a billion times
magnified, we would see that from its own point of view it is always changing:
molecules are leaving the surface, molecules are coming back.
Why do we see no change? Because just as many molecules are leaving as are
coming back! In the long run “nothing happens.” If we then take the top of the
vessel off and blow the moist air away, replacing it with dry air, then the number
of molecules leaving is just the same as it was before, because this depends on
the jiggling of the water, but the number coming back is greatly reduced because
there are so many fewer water molecules above the water. Therefore there are
more going out than coming in, and the water evaporates. Hence, if you wish to
evaporate water turn on the fan!
Here is something else: Which molecules leave? When a molecule leaves it
is due to an accidental, extra accumulation of a little bit more than ordinary
energy, which it needs if it is to break away from the attractions of its neighbors.
Therefore, since those that leave have more energy than the average, the ones that
are left have less average motion than they had before. So the liquid gradually
1-5
cools if it evaporates. Of course, when a molecule of vapor comes from the air to
the water below there is a sudden great attraction as the molecule approaches the
surface. This speeds up the incoming molecule and results in generation of heat.
So when they leave they take away heat; when they come back they generate
heat. Of course when there is no net evaporation the result is nothing—the
water is not changing temperature. If we blow on the water so as to maintain a
continuous preponderance in the number evaporating, then the water is cooled.
Hence, blow on soup to cool it!
SALT DISSOLVING IN WATER
CHLORINE SODIUM
Figure 1-6
Of course you should realize that the processes just described are more
complicated than we have indicated. Not only does the water go into the air, but
also, from time to time, one of the oxygen or nitrogen molecules will come in and
“get lost” in the mass of water molecules, and work its way into the water. Thus
the air dissolves in the water; oxygen and nitrogen molecules will work their way
into the water and the water will contain air. If we suddenly take the air away
from the vessel, then the air molecules will leave more rapidly than they come in,
and in doing so will make bubbles. This is very bad for divers, as you may know.
Crystal • ◦ a (˚A)
Rocksalt Na Cl 5.64
Sylvine K Cl 6.28
Ag Cl 5.54
Mg O 4.20
Galena Pb S 5.97
Pb Se 6.14
Pb Te 6.34
Nearest neighbor
distance d = a/2
x
y
z
a
d 1
2
3
4
5
6
7
8
Figure 1-7
Now we go on to another process. In Fig. 1-6 we see, from an atomic point
of view, a solid dissolving in water. If we put a crystal of salt in the water, what
will happen? Salt is a solid, a crystal, an organized arrangement of “salt atoms.”
Figure 1-7 is an illustration of the three-dimensional structure of common salt,
sodium chloride. Strictly speaking, the crystal is not made of atoms, but of what
we call ions. An ion is an atom which either has a few extra electrons or has lost a
few electrons. In a salt crystal we find chlorine ions (chlorine atoms with an extra
electron) and sodium ions (sodium atoms with one electron missing). The ions all
stick together by electrical attraction in the solid salt, but when we put them in
the water we find, because of the attractions of the negative oxygen and positive
hydrogen for the ions, that some of the ions jiggle loose. In Fig. 1-6 we see a
chlorine ion getting loose, and other atoms floating in the water in the form of ions.
This picture was made with some care. Notice, for example, that the hydrogen
ends of the water molecules are more likely to be near the chlorine ion, while near
the sodium ion we are more likely to find the oxygen end, because the sodium is
positive and the oxygen end of the water is negative, and they attract electrically.
Can we tell from this picture whether the salt is dissolving in water or crystallizing
out of water? Of course we cannot tell, because while some of the atoms are
leaving the crystal other atoms are rejoining it. The process is a dynamic one,
just as in the case of evaporation, and it depends on whether there is more or
less salt in the water than the amount needed for equilibrium. By equilibrium we
mean that situation in which the rate at which atoms are leaving just matches
the rate at which they are coming back. If there is almost no salt in the water,
more atoms leave than return, and the salt dissolves. If, on the other hand, there
are too many “salt atoms,” more return than leave, and the salt is crystallizing.
In passing, we mention that the concept of a molecule of a substance is only
approximate and exists only for a certain class of substances. It is clear in the
case of water that the three atoms are actually stuck together. It is not so clear in
the case of sodium chloride in the solid. There is just an arrangement of sodium
and chlorine ions in a cubic pattern. There is no natural way to group them as
“molecules of salt.”
Returning to our discussion of solution and precipitation, if we increase the
temperature of the salt solution, then the rate at which atoms are taken away
is increased, and so is the rate at which atoms are brought back. It turns out
to be very difficult, in general, to predict which way it is going to go, whether
more or less of the solid will dissolve. Most substances dissolve more, but some
substances dissolve less, as the temperature increases.'''

language = 'en'

myobj = gTTS(text=text, lang=language, slow=False)
myobj.save(r'D:\book audio\The Feynman Lectures on Physics, Volume 1_ Mainly Mechanics, Radiation\1.3 Atomic processes.mp3')