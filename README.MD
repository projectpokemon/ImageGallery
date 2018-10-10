# Project Pokémon Image Gallery

This repository of images is the source of the Project Pokémon Image Gallery.

## Current directories

* ~/Pokedex - This directory is automatically published to the [Image-dex](https://projectpokemon.org/home/gallery/category/2-image-dex/) section of our site.
* ~/Resources - This directory contains files used in the creation and sorting of images. Right now, it's where we put SVGs that we turn into more common formats.
* ~/Unfiled - This is where we put images that have not been sorted into one of the other directories yet. Assistance is appreciated.

## File structure
### ~/Pokedex
To aid our automated publisher, we keep a strict format of everything in this directory.

#### Folders
Directories must be the name of a Pokémon or other creature, as they will be the name of a gallery album on our website.

Subdirectories inside these directories are not allowed.

Folders may have the following name structures:
* [Name]
* [DexID] [Name]

This lets us tag images with [Name], for easier searching.

#### Files
Images are the primary aggregates, and other files that share the same name provide metadata. The following extensions are supported:
* *.gif, *.jpeg, *.jpe, *.jpg, *.png - These are image files (obviously). The name of this file is the name of the image as it appears on our website.
* *.txt - This file contains a description of the image. HTML is allowed and encouraged.
* *.credit - This file contains a brief description of who should be credited for the image. HTML is not allowed.
* *.tags - This file contains a comma-separated list of tags, to make searching for images easier.
* *.exclude - Files with this extension are ignored

## Contributing

We would love your help in sourcing and organizing these images. If you're willing, please use these steps to contribute:

1. Fork the repository
2. Commit changes within the guidelines above
3. Make a pull request to the master branch

A collaborator will then review your changes to make sure our automated publisher won't choke, and we will then merge your pull request. Members of Project Pokémon may receive the Image Contributor award to recognize your contribution.
