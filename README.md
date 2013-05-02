#AetherSphereEngine

A simulation engine to underly other projects.

#Those Other Projects
* AetherSphere: Massively mutiplayer spaceflight and combat sim. Multiple pocket universes that can be jumped to and from, some with a aether like drag effects for flight sim style interaction and othes with more correct Newtoninan physics. Ships and other objects will be modeled as spheres for collision and drag purposes, possibly with no orientation to simplifiy computation. Ships will be built up from components such as engines, propellant tanks, power supplies, weaponry, heat radiators and shields. Weaponry will include projectile mass driver weapons and guided missiles. Shields will be energy resevoirs that must disipate heat to remain in action and will convert all of a projectile's relative kinectic energy into heat, which then must be dissipated by the ship's radiators.

* SWAG-In-A-Box: A 6-dof model aircraft design and optimization toolset.

* N-way soccer simulation: For developing AIs and playing around with player modelling.

* SkyBlazer: A 6-dof launch vehicle sim and trajectory optimizer.

#Philosophy 
* Emphasis on flexiblity and precision over speed. Designed specifically with arbitrary precision numerics in mind.
* Elegant, clear, accessible and well documented code.
* All objects/data types serializable. Probably with JSON
* Mostly language agnostic with a strong foreign function/multi language interfaces. Probably multilingual, too. I want to play around with Haskell, Julia and Rust in addition to Python.
* Scalable across multiple processors and sytems
* Considerable independence from 3rd party toolkits.

#Organziation
* Each project will have it's own directory with common utilities being built into the AetherSphereEngine, which will also have it's own directory. Each project will have it's own Readme and similar files as well.

#Plan of action
Implement each of the above projects while designing, creating and extending the engine while keeping the overall applications in mind. I'm going to attack SkyBlazer first, I think.
