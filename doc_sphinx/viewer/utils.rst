============================
Getters and utils methods
============================

.. contents::
   :depth: 3

Syntax
=============

Getters allow to quickly get information about objects of the scene. They are reachable using this syntax:

.. code-block:: javascript

    this.$utils.getterIWantToAccess(someParameter);

Getters
===========

Here is a list of all the getters:

Get scene objects
-----------------------

.. code-block:: javascript

    /**
     * Get all scene objects.
     * @return {Map<string, object>} a Map with all id as keys and object as values.
     */
    getAllObjects();

Get objects IDs
--------------------

.. code-block:: javascript

    /**
     * Get all scene object ids.
     * @return {Array<string>} all scene object ids.
     */
    getAllIds();

Get objects by type
---------------------

Get all scene objects of a specific type.

.. code-block:: javascript

    /**
     * Get all scene objects of a specific type.
     * @param {string} type - a specific type.
     * @return {Array<object>} all scene objects of specific type.
     */
    getAllObjectsOfType(type);

Get types by IDs
-----------------

.. code-block:: javascript

    /**
     * Get all types of ids.
     * @param {Array|Set<string>} ids
     * @return {Array<string>} Types of ids.
     */
    getTypesOf(ids);

Get IDs by type
-----------------

Get all objects ids that share the same IfcType than an object received in parameter.

.. code-block:: javascript

    /**
     * Get all objects ids that share the same IfcType than an object received in parameter.
     * @param {Array|Set<string>} ids - object ids inspected for their IfcTypes.
     * @return {Array<string>} object ids with the same IfcTypes as objects of ids received in parameter.
     */
    getIdsByTypeOf(ids);

Get icfId
--------------

Get the icfId the object id belongs to.

.. code-block:: javascript

    /**
     * Get the icfId the object id belongs to.
     * @param {string} id - an object id.
     * @return {number} the icfId the object id belongs to.
     */
    getIfcIdOf(id);

Get object by id
-----------------

Get an object from its ID.

.. code-block:: javascript

    /**
     * Get object by id.
     * @param {string} id - an object id.
     * @return {object} an object with this id.
     */
    getObject(id);

Get the object's name
----------------------

.. code-block:: javascript

    /**
     * Get object's name.
     * @param {string} id - an object id.
     * @return {string} the object's name.
     */
    getObjectName(id);


Get selected IDs
------------------

Get all selected Ids. (the same property is present on the store state but it is a Set instead of an Array).

.. code-block:: javascript

    /**
     * Get all selected Ids.
     * @return {Array<string>} selected object ids.
     */
    getSelectedObjectIds();


Structure
===========

Get structure
----------------

.. code-block:: javascript

    /**
     * Get the structure of an object id.
     * @param {string} id - an object id.
     * @return {object} the corresponding structure.
     */
    getStructureOf(id);

Get the parent
--------------------

.. code-block:: javascript

    /**
     * Get object parent.
     * @param {string} id - an object id.
     * @return {object} the parent of the object.
     */
    getObjectParent(id);

Get the children
------------------

.. code-block:: javascript

    /**
     * Get object children.
     * @param {string} id - an object id.
     * @return {object[]} the children of the object.
     */
    getObjectChildren();

Get the descendants
---------------------

.. code-block:: javascript

    /**
     * Get object descendants.
     * @param {string} id - an object id.
     * @return {object[]} the descendants of the object.
     */
    getObjectDescendants();

Get the ancestors
-------------------

.. code-block:: javascript

    /**
     * Get object ancestors.
     * @param {string} id - an object id.
     * @return {object[]} the descendants of the object.
     */
    getObjectAncestors();

Get an ancestor by type
--------------------------

Get the first ancestor of an object with a specific IfcType.

.. code-block:: javascript

    /**
     * Get the first ancestor of an object with a specific IfcType.
     * @param {string} id - an object id.
     * @param {string} type - an IfcType.
     * @return {object} the first ancestor of the object with a specific IfcType.
     */
    getObjectAncestorByType(id, type);

Get the storey
----------------

Get the first ancestor of an object with the IfcType "storey".
It is a shortcut, equivalent to getObjectAncestorByType(id, "storey");

.. code-block:: javascript

    /**
     * Get the first ancestor of an object with the IfcType "storey".
     * It is equivalent to getObjectAncestorByType(id, "storey");
     * @param {string} id - an object id.
     * @return {object} the first ancestor of the object with the IfcType "storey".
     */
    getObjectStorey(id);

Get the space
---------------

Get the first ancestor of an object with the IfcType "space".
It is a shortcut, equivalent to getObjectAncestorByType(id, "space");

.. code-block:: javascript

    /**
     * Get the first ancestor of an object with the IfcType "space".
     * It is equivalent to getObjectAncestorByType(id, "space");
     * @param {string} id - an object id.
     * @return {object} the first ancestor of the object with the IfcType "space".
     */
    getObjectSpace(id);


Example
=======

Clicking the plugin icon will activate the _'select by storey'_ mode. When you click an object, all objects in the same ``storey`` are selected. The hover is ``storey`` dependent.

.. code-block:: html

    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8" />
        <title>BIMData - Getters - Storey</title>
        <script
          src="https://unpkg.com/@bimdata/viewer/dist/bimdata-viewer.min.js"
          charset="utf-8"
        ></script>
      </head>

      <body>
        <div style="height: 100vh">
          <div id="app"></div>
        </div>
        <script>
          const cfg = {
            cloudId: 88,
            projectId: 100,
            ifcIds: [175],
            logo: true,
            bimdataPlugins: {
              default: false
              rightClickMenu: true,
              alerts: true,
            }
          };
          const accessToken = "DEMO_TOKEN";
          const { viewer } = initBIMDataViewer(
            "app",
            accessToken,
            cfg
          );

          viewer.registerPlugins([
            {
              name: "storey-select",
              component: {
                render() {
                  return null;
                },
                data() {
                  return {
                    pickedNothingSubscription: null,
                    pickSubscription: null,
                    hoverSubscription: null,
                    hoverOffSubscription: null,
                    highlightedStorey: null
                  };
                },
                props: ["active"],
                methods: {
                  deselectAll() {
                    this.$hub.emit("deselect-objects", {
                      ids: this.$utils.getSelectedObjectIds()
                    });
                  },
                  unhighlightAll() {
                    if (this.highlightedStorey) {
                      this.$hub.emit("unhighlight-objects", {
                        ids: this.$utils
                          .getObjectDescendants(this.highlightedStorey.uuid)
                          .map(object => object.uuid)
                      });
                      this.highlightedStorey = null;
                    }
                  }
                },
                watch: {
                  active: {
                    handler(active) {
                      const viewer3D = this.$plugins.viewer3D;
                      viewer3D.selectOnClick = !active;
                      viewer3D.highlightOnHover = !active;
                      if (active) {
                        document.body.style.setProperty(
                          "cursor",
                          "crosshair",
                          "important"
                        );
                        this.pickSubscription = viewer3D.viewer.cameraControl.on(
                          "picked",
                          pickResult => {
                            if (!pickResult || !pickResult.entity) return;
                            const storey = this.$utils.getObjectStorey(
                              pickResult.entity.id
                            );
                            if (storey) {
                              this.$hub.emit("select-objects", {
                                ids: this.$utils
                                  .getObjectDescendants(storey.uuid)
                                  .map(object => object.uuid)
                              });
                            } else {
                              this.$hub.emit("alert", {
                                type: "infos",
                                message: "No storey found for clicked object."
                              });
                            }
                          }
                        );

                        this.pickedNothingSubscription = viewer3D.viewer.cameraControl.on(
                          "pickedNothing",
                          this.deselectAll
                        );

                        this.hoverSubscription = viewer3D.viewer.cameraControl.on(
                          "hover",
                          hit => {
                            if (hit && hit.entity && hit.entity.isObject) {
                              const storey = this.$utils.getObjectStorey(
                                hit.entity.id
                              );
                              if (storey) {
                                if (
                                  !this.highlightedStorey ||
                                  storey !== this.highlightedStorey
                                ) {
                                  if (
                                    this.highlightedStorey &&
                                    storey !== this.highlightedStorey
                                  ) {
                                    this.unhighlightAll();
                                  }
                                  this.$hub.emit("highlight-objects", {
                                    ids: this.$utils
                                      .getObjectDescendants(storey.uuid)
                                      .map(object => object.uuid)
                                  });
                                  this.highlightedStorey = storey;
                                }
                              }
                            }
                          }
                        );
                        // Deselect all on hover off
                        this.hoverOffSubscription = viewer3D.viewer.cameraControl.on(
                          "hoverOff",
                          this.unhighlightAll
                        );
                      } else {
                        this.unhighlightAll();
                        document.body.style.removeProperty("cursor");
                        viewer3D.viewer.cameraControl.off(
                          this.pickedNothingSubscription
                        );
                        viewer3D.viewer.cameraControl.off(this.pickSubscription);
                        viewer3D.viewer.cameraControl.off(this.hoverSubscription);
                        viewer3D.viewer.cameraControl.off(
                          this.hoverOffSubscription
                        );
                      }
                    }
                  }
                }
              },
              display: {
                iconPosition: "right"
              },
              keepActive: true
            }
          ]);
        </script>
      </body>
    </html>
