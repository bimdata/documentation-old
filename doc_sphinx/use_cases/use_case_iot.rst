=============================================
Use Case: Enrich BIM Viewer with IoT data
=============================================

..
    excerpt
        Discover how to use the Viewer as a visualisation tool
    endexcerpt



What was the input?
======================

We have sensors for temperature and sensors for moisture placed in our building.
We have a Model of the building, locations, and pictures of the sensors. We attach every picture to a place on the Model.

We want to visualize the location of the sensors in the building.

The idea
===========

* View values on a 3D view of the building
* Use the BCF display system to display custom images.

The result
===========

Get it :download:`Download the HTML file <../_static/usecase_iot_example.html>`

See it in action
------------------

.. raw:: html
   :file: ../_static/usecase_iot_example.html

Step-by-Step
==============

1/ Init the Viewer
----------------------

We set a Viewer with some useful options:

 * ``edit: false``: no edition tools are provided
 * ``comment: false``: no comment tool is provided
 * ``camera: false``: no change camera
 * ``fullscreen: false``: no fullscreen option
 * ``property: false``: no property button is displayed

Basically, no UI interaction is needed.

.. code-block:: javascript

    options: {
        menu: {
        show_buttons: {
            comment: false,
            edit: false,
            camera: false,
            fullscreen: false,
            property: false,
        }
        }
    }

2/ Set a list of monitored elements
------------------------------------

In this recipe, we have chosen Instagram photos to associate with the elements.
The sensors are listed with their UUID to be later linked with BCF.

.. code-block:: javascript

    const monitoredElements = [
        "313IdYHbv0JwPbnB6B727$",
        "3n11jxQJbAbQWMixM04wKx",
        "2enSXdsnT8fe5rSym78nVF",
        "2Idfvppc1A1wUGKwi4iDp2"
    ];

.. note:: 
    Elements can be retrieved from an external Database.

3/ Create annotations styles
------------------------------

Creation of a JS method: ``viewer.setObjectAnnotationCSS()``
This method define CSS styles to apply to the pins and labels to apply to HTML elements.

Find the detail of this method in the Complete code below.

This method is then used in:

.. code-block:: javascript
    :linenos:

    viewer.on('viewer-load', async function (e) {
    let index = 1;
    const data = await retrieveExternalData();
    for (let uuid of monitoredElements) {
        // Create annotation for each interesting element
        let annotationId = await viewer.createObjectAnnotation(uuid, {
        spotHTML: `<div class="bimdata-annotation-pin">${index}</div>`,
        labelHTML: `<div class="bimdata-annotation-label" style="font-size: 18pt;">
            <p>${uuid}</p>
            <img src=${data.shortcode_media.display_resources[2].src}></img>
            </div>
        `
        });
        index++;
    }
    })


4/ Set the behavior onClick
----------------------------

.. code-block:: javascript
    :linenos:

    viewer.on("annotation-pin-clicked", async function (e) {
    const annotationId = e.annotationId;
    const annotationShown = await viewer.getAnnotationLabelShown(annotationId);
    viewer.hideAnnotationsLabels();
    viewer.setAnnotationLabelShown(annotationId, !annotationShown);
    });

Complete code
================

Want to try yourself?
Copy-paste this code and try it!

.. code-block:: html
    :linenos:

        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="UTF-8">
        <title>BIMData Viewer</title>
        <script src="https://cdn-beta.bimdata.io/js/bimdata-viewer-embed.js"></script>
        </head>
        <body>
        <div class="viewer-container" style="overflow: hidden;">
                <div id="embed" style="height: 100vh"></div>
        </div>
        <script type="text/javascript">

        // Example of extarnal data retrieving
        async function retrieveExternalData() {
            const url = "https://www.instagram.com/graphql/query/?query_hash=477b65a610463740ccdb83135b2014db&variables=%7B%22shortcode%22%3A%22By5YPArn5Sz%22%2C%22child_comment_count%22%3A3%2C%22fetch_comment_count%22%3A40%2C%22parent_comment_count%22%3A24%2C%22has_threaded_comments%22%3Atrue%7D"

            const response = await fetch(url);
            const json = await response.json();
                return json.data;
            }

            // Setup BIMData Viewer
            var accessToken = 'DEMO_TOKEN';
            var cloudId = 88;
            var projectId = 100;
            var ifcId = 175;

            let viewer = new window.BIMDataViewer('embed', {
            accessToken,
            cloudId,
            projectId,
            ifcId,
            options: {
                menu: {
                show_buttons: {
                    comment: false,
                    edit: false,
                    camera: false,
                    fullscreen: false,
                    property: false,
                }
                }
            }
            });

            // Example of elements with annotations.
            const monitoredElements = [
                "313IdYHbv0JwPbnB6B727$",
                "3n11jxQJbAbQWMixM04wKx",
                "2enSXdsnT8fe5rSym78nVF",
                "2Idfvppc1A1wUGKwi4iDp2"
            ];

            // Disable pre-selection of element on mouse hover
            viewer.on('mouse-hover', e => {
                e.preventDefault();
            })

            // Set Annotation CSS
            viewer.on('viewer-init', function (e) {
            viewer.setObjectAnnotationCSS(`
                .bimdata-annotation-pin {
                display: flex;
                align-items: center;
                justify-content: center;
                font-family: "Roboto", "Segoe UI", BlinkMacSystemFont, system-ui, -apple-system;
                font-size: 0.786rem;
                color: #ffffff;
                position: absolute;
                width: 25px;
                height: 25px;
                border-radius: 100%;
                border: 1px solid #ffffff;
                background: black;
                visibility: hidden;
                box-shadow: 0 2px 10px 0 rgba(0,0,0,0.07);
                z-index: 0;
                background: #00AF50;
                }
                .bimdata-annotation-label {
                    position: absolute;
                    max-width: 400px;
                    min-height: 250px;
                    padding: 8px;
                    padding-left: 12px;
                    padding-right: 12px;
                    background: white;
                    color: black;
                    -webkit-border-radius: 3px;
                    -moz-border-radius: 3px;
                    border-radius: 6px;
                    border: #ffffff solid 2px;
                    box-shadow: 0px 0px 15px 1px #222222;
                    z-index: 90000;
                }
                .bimdata-annotation-label:after {
                    content: "";
                    position: absolute;
                    border-style: solid;
                    border-width: 8px 12px 8px 0;
                    border-color: transparent darkblue;
                    display: block;
                    width: 0;
                    z-index: 1;
                    margin-top: -11px;
                    left: -12px;
                    top: 20px;
                }
                .bimdata-annotation-label:before {
                    content: "";
                    position: absolute;
                    border-style: solid;
                    border-width: 9px 13px 9px 0;
                    border-color: transparent #ffffff;
                    display: block;
                    width: 0;
                    z-index: 0;
                    margin-top: -12px;
                    left: -15px;
                    top: 20px;
                }
            `);
            });

            // When the viewer has loaded the model
            viewer.on('viewer-load', async function (e) {
            let index = 1;
            const data = await retrieveExternalData();
            for (let uuid of monitoredElements) {
                // Create annotation for each interesting element
                let annotationId = await viewer.createObjectAnnotation(uuid, {
                spotHTML: `<div class="bimdata-annotation-pin">${index}</div>`,
                labelHTML: `<div class="bimdata-annotation-label" style="font-size: 18pt;">
                    <p>${uuid}</p>
                    <img src=${data.shortcode_media.display_resources[2].src}></img>
                    </div>
                `});
                index++;
            }
            })

            // Opening the annotation detail on pin click
            viewer.on("annotation-pin-clicked", async function (e) {
                const annotationId = e.annotationId;
                const annotationShown = await viewer.getAnnotationLabelShown(annotationId);
                viewer.hideAnnotationsLabels();
                viewer.setAnnotationLabelShown(annotationId, !annotationShown);
            });

            // Close annotation detail on click away
            viewer.on('mouse-click-nothing', e => {
                viewer.hideAnnotationsLabels();
            });

        </script>
        </body>
        </html>
