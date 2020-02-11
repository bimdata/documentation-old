============================
Events
============================

You can emit custom events using the hub:

.. code-block:: javascript

    this.$hub.emit("my-event", payload);

You can listen to events the same way:

.. code-block:: javascript

    this.$hub.on("my-event", callback);

Default plugins are using events that you can also emit or listen. Use them to interact with default plugins or the 3D engine.

.. code-block:: javascript

    /**
     * Set the projection type
     * @param {string} projection - possible values: perspective | ortho
     */
    $hub.emit("set-projection-type", { projection });

.. code-block:: javascript

    /**
     * Set section mode.
     * @param {boolean} active - true when section mode is active.
     */
    $hub.emit("set-section-mode", { active });

.. code-block:: javascript

    /**
     * Create a section plane.
     * options can be either axis or direction AND position.
     * @param {string} options.axis - an axis on wich to create section plane. Possible values: "x" | "y" | "z".
     * @param {Float32Array(3)} options.direction
     * @param {Float32Array(3)} options.position
     */
    $hub.emit("create-section-plane", options);

.. code-block:: javascript

    /**
     * Delete the active section plane.
     */
    $hub.emit("delete-section-plane");

.. code-block:: javascript

    /**
     * Delete all section planes.
     */
    $hub.emit("delete-all-section-planes");

.. code-block:: javascript

    /**
     * Select object ids.
     * @param {Array|Set<string>} ids - the ids of objects to select.
     */
    $hub.emit("select-objects", { ids });

.. code-block:: javascript

    /**
     * Deselect object ids.
     * @param {Array|Set<string>} ids - the ids of objects to deselect.
     */
    $hub.emit("deselect-objects", { ids });

.. code-block:: javascript

    /**
     * Show objects.
     * @param {Array|Set<string>} ids - the ids of objects to show.
     */
    $hub.emit("show-objects", { ids });

.. code-block:: javascript

    /**
     * Hide objects.
     * @param {Array|Set<string>} ids - the ids of objects to hide.
     */
    $hub.emit("hide-objects", { ids });

.. code-block:: javascript

    /**
     * Highlight objects.
     * @param {Array|Set<string>} ids - the ids of objects to highlight.
     */
    $hub.emit("highlight-objects", { ids });

.. code-block:: javascript

    /**
     * Unhighlight objects.
     * @param {Array|Set<string>} ids - the ids of objects to unhighlight.
     */
    $hub.emit("unhighlight-objects", { ids });

.. code-block:: javascript

    /**
     * Colorize objects.
     * @param {Array|Set<string>} ids - the ids of objects to colorize.
     * @param {Array(3)} color - the color to apply on objects.
     */
    $hub.emit("colorize-objects", { ids, color });

.. code-block:: javascript

    /**
     * Set viewpoint.
     * @param {object} viewpoint - the viewpoint to set (https://xeokit.github.io/xeokit-sdk/docs/class/src/plugins/BCFViewpointsPlugin/BCFViewpointsPlugin.js~BCFViewpointsPlugin.html)
     */
    $hub.emit("set-viewpoint", viewpoint);

.. code-block:: javascript

    /**
     * Fit view on objects.
     * @param {Array|Set<string>} ids - the ids of objects to fit the view.
     */
    $hub.emit("fit-view-objects", { ids });

.. code-block:: javascript

    /**
     * Isolate objects.
     * @param {Array|Set<string>} ids - the ids of objects to isolate.
     */
    $hub.emit("isolate-objects", { ids });

.. code-block:: javascript

    /**
     * Unisolate all objects.
     */
    $hub.emit("unisolate-all-objects");

.. code-block:: javascript

    /**
     * Create annotations.
     * @param {Array|Set<string>} ids - the ids of objects on wich to create annotation.
     * @param {number|string} index - the index that will be displayed on annotations.
     * @param {string} priority - the priority that will change the annotation aspect. Possible Values: "low" | "medium" | "hight"
     */
    $hub.emit("create-annotations", { ids, index, priority });

.. code-block:: javascript

    /**
     * Delete all annotations.
     */
    $hub.emit("clear-annotations");
