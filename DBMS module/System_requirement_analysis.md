# The ER Model
The basic purpose of the conceptual ER model is then to establish structural metadata com-
monality for the master data entities between the set of logical ER models. The conceptual data
model is used to form commonality relationships between ER models as a basis for data model
integration.

<p align="center">
<img width="700" height="535" src="/images/ER-model.png"> 
  </p>

## Entitities
The above ER model is designed with two fundamental
entities:
1. **Properties** - The properties or the assets are one of the basic entities on which the system is
being built upon. The various attributes are so chosen to get the clear recognizable property
of the user’s desired as and when required. The Prop.ID will uniquely identify the specific
property or the asset from the database along with the complete details that includes its
establishment date and the managing staff for the particular property. The property entity
has been framed with the following attributes:
    * Prop. ID
    * Property Name
    * Location
    * Establishment Date
    * Description

2. **Users**: As it is clear from above that the users entity supports ***ISA Relationship*** types.
An ISA relationship suggests that when an entity type contains certain entities thathave
special properties not shared by all entities, this suggests two entity types should be created
with an ISA relationship type between them. Here, with reference to this system under the
project, we can say that the user entity is in ISA relationship with the Superuser, Admin
Staffs and Real World Users. All the three party users of the system have their own charaterized features and attributes, but one thing that is common in all is the ID. This ID
uniquely defines each one of them, subsequently helpful for differentiating among themselves.
For instance, let’s take the scenario of a member of the system and we want to know whether
it’s an admin staff or the maintainer, in such a case the specific ID provided will help us to
know their identity.
    * Superuser
    * Admin
    * Real World Users
