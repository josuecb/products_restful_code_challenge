/**
 * Created by Josue at 3/12/2018
 **/

$(document).ready(function () {
    var buildDbBtn = $('#build-db-btn');
    var popuDbBtn = $('#populate-db-btn');
    var delDbBtn = $('#delete-db-btn');

    var addBtn = $('#add-btb');
    var findbyIdBtn = $('#find-by-id-btn');
    var updateBtn = $('#update-btn');
    var delBtn = $('#delete-btn');
    var gelAllBtn = $('#get-all-btn');
    var findByNameBtn = $('#find-by-name-btn');
    var addAttrBtn = $('#add-attr-btn');
    var delAttrBtn = $('#del-attr-btn');

    var avw = $('#action-view-wrapper');
    var cvw = $('#content-view-wrapper');
    var aat = $('#api-action-title');
    var msh = $('#message-system-content > div');

    requestProductAttributes();

    buildDbBtn.on('click', function () {
        var xhr = new XMLHttpRequest();

        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                try {
                    var response = readBody(xhr);
                    console.log(response);
                    messageView(response, 'success-color')
                } catch (e) {
                    throw "This is not a json object"
                }
            } else if (xhr.readyState === XMLHttpRequest.DONE && xhr.status > 400) {
                console.log("An error occurred");
                messageView("An error occurred", 'warning-color');
                console.log(readBody(xhr))
            }


        };

        xhr.open('GET', '/api/build_database/', true);
        xhr.send();
    });

    popuDbBtn.on('click', function () {
        var xhr = new XMLHttpRequest();

        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                try {
                    var response = readBody(xhr);
                    console.log(response);
                    messageView(response, 'success-color');
                    requestProductAttributes()
                } catch (e) {
                    throw "This is not a json object"
                }
            } else if (xhr.readyState === XMLHttpRequest.DONE && xhr.status > 400) {
                console.log("An error occurred");
                messageView("An error occurred", 'warning-color');
                console.log(readBody(xhr))
            }


        };

        xhr.open('GET', '/api/populate_database/', true);
        xhr.send();
    });

    delDbBtn.on('click', function () {
        var xhr = new XMLHttpRequest();

        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                try {
                    var response = readBody(xhr);
                    console.log(response);
                    messageView(response, 'success-color');
                    requestProductAttributes()
                } catch (e) {
                    throw "This is not a json object"
                }
            } else if (xhr.readyState === XMLHttpRequest.DONE && xhr.status > 400) {
                console.log("An error occurred");
                messageView("An error occurred", 'warning-color');
                console.log(readBody(xhr))
            }


        };

        xhr.open('GET', '/api/delete_database/', true);
        xhr.send();
    });

    addBtn.on('click', function () {
        /**
         * Building UI
         * @type {*|jQuery|HTMLElement}
         */
        // Changing title
        aat.html('<span>API Actions (Creating new Product)</span>');
        avw.html('');   // Clearing previous content in view

        var inputName = $('<input>', {
            type: 'text',
            name: 'product_name',
            placeholder: 'Product Name:',
        });

        inputName.appendTo(avw);

        var inputPrice = $('<input>', {
            type: 'text',
            name: 'product_price',
            placeholder: 'Product Price:',
        });
        inputPrice.appendTo(avw);

        var inputCategory = $('<input>', {
            type: 'text',
            name: 'product_category',
            placeholder: 'Product Category:',
        });

        inputCategory.appendTo(avw);

        var btnHolder = $('<div></div>', {class: 'button-wrapper'});
        var insertBtn = $('<button></button>', {
            name: 'action',
            value: 'create',
        });

        insertBtn.html("Create");

        insertBtn.appendTo(btnHolder);
        btnHolder.appendTo(avw);

        /**
         * Action when inserting item
         */

        insertBtn.on('click', function () {
            console.log("clicking create button");
            if (inputName.val() === '' || inputName.val() === undefined) {
                alert("Name is empty.")
            } else if (inputPrice.val() === '' || inputPrice.val() === undefined) {
                alert("Price is empty.")
            } else {
                var xhr = new XMLHttpRequest();
                var form = createForm({
                    product_name: inputName.val(),
                    product_price: inputPrice.val(),
                    product_category: inputCategory.val(),
                });

                xhr.onreadystatechange = function () {
                    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                        try {
                            var response = readBody(xhr);
                            console.log(response);
                            messageView(response, 'success-color');

                            // Clearing value from input
                            inputName.val('');
                            inputPrice.val('');
                            inputCategory.val('');

                            // Updating Product list
                            requestProductAttributes()
                        } catch (e) {
                            throw "This is not a json object"
                        }
                    } else if (xhr.readyState === XMLHttpRequest.DONE && xhr.status > 400) {
                        console.log("An error occurred");
                        messageView("An error occurred", 'warning-color');
                        console.log(readBody(xhr))
                    }


                };

                xhr.open('POST', '/api/create/', true);
                xhr.send(new FormData(form));
            }
        });


    });

    updateBtn.on('click', function () {
        /**
         * Building UI
         * @type {*|jQuery|HTMLElement}
         */
        // Changing title
        aat.html('<span>API Actions (Modify Existing Product)</span>');
        avw.html('');   // Clearing previous content in view

        var inputId = $('<input>', {
            type: 'text',
            name: 'product_id',
            placeholder: 'Existing Product Id:',
        });

        inputId.appendTo(avw);

        var inputName = $('<input>', {
            type: 'text',
            name: 'product_name',
            placeholder: 'Product Name:',
        });

        inputName.appendTo(avw);

        var inputPrice = $('<input>', {
            type: 'text',
            name: 'product_price',
            placeholder: 'Product Price:',
        });
        inputPrice.appendTo(avw);

        var inputCategory = $('<input>', {
            type: 'text',
            name: 'product_category',
            placeholder: 'Product Category:',
        });

        inputCategory.appendTo(avw);

        var btnHolder = $('<div></div>', {class: 'button-wrapper'});
        var insertBtn = $('<button></button>', {
            name: 'action',
            value: 'create',
        });

        insertBtn.html("Update");

        insertBtn.appendTo(btnHolder);
        btnHolder.appendTo(avw);

        /**
         * Action when inserting item
         */

        insertBtn.on('click', function () {
            console.log("clicking create button");
            if (inputId.val() === '' || inputId.val() === undefined) {
                alert("Id is empty.")
            } else if (inputName.val() === '' || inputName.val() === undefined) {
                alert("Name is empty.")
            } else if (inputPrice.val() === '' || inputPrice.val() === undefined) {
                alert("Price is empty.")
            } else {
                var xhr = new XMLHttpRequest();
                var form = createForm({
                    product_id: inputId.val(),
                    product_name: inputName.val(),
                    product_price: inputPrice.val(),
                    product_category: inputCategory.val(),
                });

                xhr.onreadystatechange = function () {
                    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                        try {
                            var response = readBody(xhr);
                            console.log(response);
                            messageView(response, 'success-color');
                            // Clearing value from input
                            inputId.val('');
                            inputName.val('');
                            inputPrice.val('');
                            inputCategory.val('');

                            // Updating Product list
                            requestProductList()
                        } catch (e) {
                            throw "This is not a json object"
                        }
                    } else if (xhr.readyState === XMLHttpRequest.DONE && xhr.status > 400) {
                        console.log("An error occurred");
                        messageView("An error occurred", 'warning-color');
                        console.log(readBody(xhr))
                    }


                };

                xhr.open('UPDATE', '/api/update/', true);
                xhr.send(new FormData(form));
            }
        });

    });

    findbyIdBtn.on('click', function () {
        /**
         * Building UI
         * @type {*|jQuery|HTMLElement}
         */
        // Changing title
        aat.html('<span>API Actions (Find Product by ID)</span>');
        avw.html('');   // Clearing previous content in view

        var inputId = $('<input>', {
            type: 'text',
            name: 'product_id',
            placeholder: 'Product Id:',
        });

        inputId.appendTo(avw);


        var btnHolder = $('<div></div>', {class: 'button-wrapper'});
        var insertBtn = $('<button></button>', {
            name: 'action',
            value: 'read',
        });

        insertBtn.html("Read");

        insertBtn.appendTo(btnHolder);
        btnHolder.appendTo(avw);

        /**
         * Action when inserting item
         */

        insertBtn.on('click', function () {
            console.log("clicking read button");
            if (inputId.val() === '' || inputId.val() === undefined) {
                alert("Name is empty.")
            } else {
                var xhr = new XMLHttpRequest();

                xhr.onreadystatechange = function () {
                    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                        try {
                            var response = readBody(xhr);
                            console.log(response);
                            messageView(response, 'success-color');
                            inputId.val('');
                        } catch (e) {
                            throw "This is not a json object"
                        }
                    } else if (xhr.readyState === XMLHttpRequest.DONE && xhr.status > 400) {
                        console.log("An error occurred");
                        messageView("An error occurred", 'warning-color');
                        console.log(readBody(xhr))
                    }
                };

                xhr.open('GET', '/api/read/' + inputId.val(), true);
                xhr.send();
            }
        });

    });

    delBtn.on('click', function () {
        /**
         * Building UI
         * @type {*|jQuery|HTMLElement}
         */
        // Changing title
        aat.html('<span>API Actions (Delete Product)</span>');
        avw.html('');   // Clearing previous content in view

        var inputName = $('<input>', {
            type: 'text',
            name: 'product_name',
            placeholder: 'Existing Product Name:',
        });

        inputName.appendTo(avw);


        var btnHolder = $('<div></div>', {class: 'button-wrapper'});
        var insertBtn = $('<button></button>', {
            name: 'action',
            value: 'delete',
        });

        insertBtn.html("Delete");

        insertBtn.appendTo(btnHolder);
        btnHolder.appendTo(avw);

        /**
         * Action when inserting item
         */

        insertBtn.on('click', function () {
            console.log("clicking deleting button");
            if (inputName.val() === '' || inputName.val() === undefined) {
                alert("Name is empty.")
            } else {
                var xhr = new XMLHttpRequest();

                xhr.onreadystatechange = function () {
                    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                        try {
                            var response = readBody(xhr);
                            console.log(response);
                            messageView(response, 'success-color');
                            inputName.val('');
                            requestProductAttributes()
                        } catch (e) {
                            throw "This is not a json object"
                        }
                    } else if (xhr.readyState === XMLHttpRequest.DONE && xhr.status > 400) {
                        console.log("An error occurred");
                        messageView("An error occurred", 'warning-color');
                        console.log(readBody(xhr))
                    }
                };

                xhr.open('DELETE', '/api/delete/' + inputName.val(), true);
                xhr.send();
            }
        });

    });

    findByNameBtn.on('click', function () {
        /**
         * Building UI
         * @type {*|jQuery|HTMLElement}
         */
        // Changing title
        aat.html('<span>API Actions (Search Product by Name)</span>');
        avw.html('');   // Clearing previous content in view

        var inputName = $('<input>', {
            type: 'text',
            name: 'product_name',
            placeholder: 'Existing Product Name:',
        });

        inputName.appendTo(avw);


        var btnHolder = $('<div></div>', {class: 'button-wrapper'});
        var insertBtn = $('<button></button>', {
            name: 'action',
            value: 'delete',
        });

        insertBtn.html("Search");

        insertBtn.appendTo(btnHolder);
        btnHolder.appendTo(avw);

        /**
         * Action when inserting item
         */

        insertBtn.on('click', function () {
            console.log("clicking deleting button");
            if (inputName.val() === '' || inputName.val() === undefined) {
                alert("Name is empty.")
            } else {
                var xhr = new XMLHttpRequest();

                xhr.onreadystatechange = function () {
                    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                        try {
                            var response = readBody(xhr);
                            console.log(response);
                            messageView(response, 'success-color');
                            inputName.val('');
                        } catch (e) {
                            throw "This is not a json object"
                        }
                    } else if (xhr.readyState === XMLHttpRequest.DONE && xhr.status > 400) {
                        console.log("An error occurred");
                        messageView("An error occurred", 'warning-color');
                        console.log(readBody(xhr))
                    }
                };

                xhr.open('GET', '/api/search/' + inputName.val(), true);
                xhr.send();
            }
        });

    });

    gelAllBtn.on('click', function () {
        requestProductAttributes()
    });

    addAttrBtn.on('click', function () {
        /**
         * Building UI
         * @type {*|jQuery|HTMLElement}
         */
        // Changing title
        aat.html('<span>API Actions (Add Product Attribute)</span>');
        avw.html('');   // Clearing previous content in view

        var inputAttrName = $('<input>', {
            type: 'text',
            name: 'attribute_name',
            placeholder: 'New Attribute Name:',
        });

        inputAttrName.appendTo(avw);


        var inputAttrDescription = $('<input>', {
            type: 'text',
            name: 'attribute_description',
            placeholder: 'Attribute Description:',
        });

        inputAttrDescription.appendTo(avw);


        var btnHolder = $('<div></div>', {class: 'button-wrapper'});
        var insertBtn = $('<button></button>', {
            name: 'action',
            value: 'add_attribute',
        });

        insertBtn.html("Add Attribute");

        insertBtn.appendTo(btnHolder);
        btnHolder.appendTo(avw);

        /**
         * Action when inserting item
         */

        insertBtn.on('click', function () {
            console.log("clicking create button");
            if (inputAttrName.val() === '' || inputAttrName.val() === undefined) {
                alert("Attribute Name is empty.")
            } else if (inputAttrDescription.val() === '' || inputAttrDescription.val() === undefined) {
                alert("Attribute Description is empty.")
            } else {
                var xhr = new XMLHttpRequest();
                var form = createForm({
                    attribute_name: inputAttrName.val(),
                    attribute_description: inputAttrDescription.val(),
                });

                xhr.onreadystatechange = function () {
                    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                        try {
                            var response = readBody(xhr);
                            console.log(response);
                            // Clearing value from input
                            inputAttrName.val('');
                            inputAttrDescription.val('');
                            messageView(response, 'success-color');
                            // Updating Product list
                            requestProductAttributes()
                        } catch (e) {
                            throw "This is not a json object"
                        }
                    } else if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 403) {
                        console.log("An error ocurred");
                        console.log(readBody(xhr))
                    }


                };

                xhr.open('UPDATE', '/api/add_attribute/', true);
                xhr.send(new FormData(form));
            }
        });


    });

    delAttrBtn.on('click', function () {
        /**
         * Building UI
         * @type {*|jQuery|HTMLElement}
         */
        // Changing title
        aat.html('<span>API Actions (Remove Product Attribute)</span>');
        avw.html('');   // Clearing previous content in view

        var inputAttrName = $('<input>', {
            type: 'text',
            name: 'attribute_name',
            placeholder: 'Attribute Name:',
        });

        inputAttrName.appendTo(avw);


        var btnHolder = $('<div></div>', {class: 'button-wrapper'});
        var insertBtn = $('<button></button>', {
            name: 'action',
            value: 'delete',
        });

        insertBtn.html("Delete");

        insertBtn.appendTo(btnHolder);
        btnHolder.appendTo(avw);

        /**
         * Action when inserting item
         */

        insertBtn.on('click', function () {
            console.log("clicking create button");
            if (inputAttrName.val() === '' || inputAttrName.val() === undefined) {
                alert("Attribute Name is empty.")
            } else {
                var xhr = new XMLHttpRequest();

                xhr.onreadystatechange = function () {
                    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                        try {
                            var response = readBody(xhr);
                            console.log(response);
                            // Clearing value from input
                            inputAttrName.val('');
                            messageView(response, 'success-color');
                            // Updating Product list
                            requestProductAttributes()
                        } catch (e) {
                            throw "This is not a json object"
                        }
                    } else if (xhr.readyState === XMLHttpRequest.DONE && xhr.status > 400) {
                        console.log("An error occurred");
                        messageView("An error occurred", 'warning-color');
                        console.log(readBody(xhr))
                    }


                };

                xhr.open('DELETE', '/api/delete_attribute/' + inputAttrName.val(), true);
                xhr.send();
            }
        });


    });

    function messageView(text, color) {
        // avoid undefined color
        if (color === undefined)
            color = '';

        msh.html('');    // clearing message view

        var textContainer = $('<div></div>', {class: color + " message-view"});
        var messageText = $('<span></span>');

        messageText.html(text);
        messageText.appendTo(textContainer);

        textContainer.appendTo(msh);
    }

    function attributeView(attr) {
        var itemContainer = $('<div></div>', {
            id: 'item-' + attr,
            class: 'item-container'
        });

        var itemTitleContainer = $('<div></div>', {
            class: 'item-title'
        });

        var itemText = $('<span></span>');

        var itemsHolder = $('<div></div>', {
            class: 'items-holder'
        });

        itemText.html(attr[0].toUpperCase() + attr.substr(1, attr.length));
        itemText.appendTo(itemTitleContainer);

        itemTitleContainer.appendTo(itemContainer);
        itemsHolder.appendTo(itemContainer);

        itemContainer.appendTo(cvw);
    }

    function requestProductAttributes() {
        clearingItemListView()
        var xhr = new XMLHttpRequest();

        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                try {
                    var attributes = JSON.parse(readBody(xhr));
                    for (var index in attributes) {
                        // Populate after timestamp
                        if (index == '3') {
                            attributeView('category');
                            console.log('category');
                        } else {
                            console.log(attributes[index]);
                            attributeView(attributes[index]);
                        }
                    }

                    requestProductList()
                } catch (e) {
                    throw "This is not a json object"
                }
            } else if (xhr.readyState === XMLHttpRequest.DONE && xhr.status > 400) {
                console.log("An error occurred");
                messageView("Database is empty or doesn't exist. Build it.", 'warning-color');
                console.log(readBody(xhr))
            }


        };

        xhr.open('GET', '/api/get_attributes/', true);
        xhr.send();
    }

    function requestProductList() {
        console.log("clicking");
        var xhr = new XMLHttpRequest();

        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                try {
                    var products = JSON.parse(readBody(xhr));
                    for (var index in products) {
                        populateItemList(products[index]);
                        console.log(products[index].category)
                    }
                } catch (e) {
                    throw "This is not a json object"
                }
            } else if (xhr.readyState === XMLHttpRequest.DONE && xhr.status > 400) {
                console.log("An error occurred");
                messageView("An error occurred", 'warning-color');
                console.log(readBody(xhr))
            }


        };

        xhr.open('GET', '/api/products/', true);
        xhr.send();
    }

    function clearingItemListView() {
        // Cleaning previous items
        cvw.html('')
    }

    function populateItemList(item) {
        /**
         * Populating Id
         * @type {*|jQuery|HTMLElement}
         */
        var itemIdHolder = $('#item-id > div.items-holder');
        // We need to use this item id in future for deleting the item
        var itemView = $('<div></div>', {class: 'item-text', id: 'item-id-' + item.id});
        var itemText = $('<span></span>');
        itemText.html(item.id);
        itemText.appendTo(itemView);

        itemView.appendTo(itemIdHolder);

        /**
         * Populating Name
         * @type {*|jQuery|HTMLElement}
         */
        var itemNameHolder = $('#item-name > div.items-holder');

        var itemView = $('<div></div>', {class: 'item-text', id: 'item-id-' + item.id});
        var itemText = $('<span></span>');
        itemText.html(item.name);
        itemText.appendTo(itemView);

        itemView.appendTo(itemNameHolder);

        /**
         * Populating Price
         * @type {*|jQuery|HTMLElement}
         */
        var itemPriceHolder = $('#item-price > div.items-holder');

        var itemView = $('<div></div>', {class: 'item-text', id: 'item-id-' + item.id});
        var itemText = $('<span></span>');
        itemText.html(item.price);
        itemText.appendTo(itemView);

        itemView.appendTo(itemPriceHolder);

        /**
         * Populating Category
         * @type {*|jQuery|HTMLElement}
         */
        var itemCategoryHolder = $('#item-category > div.items-holder');

        var itemView = $('<div></div>', {class: 'item-text', id: 'item-id-' + item.id});
        var itemText = $('<span></span>');
        itemText.html(item.category);
        itemText.appendTo(itemView);

        itemView.appendTo(itemCategoryHolder);
    }

    function readBody(xhr) {
        var data;
        if (!xhr.responseType || xhr.responseType === "text") {
            data = xhr.responseText;
        } else if (xhr.responseType === "document") {
            data = xhr.responseXML;
        } else {
            data = xhr.response;
        }
        return data;
    }

    /**
     * Creates a form to submit
     * @param data
     * @returns {HTMLFormElement}
     */
    function createForm(data) {
        var mForm = document.createElement('form');

        for (var key in data) {
            var p_input = document.createElement('input');
            p_input.setAttribute('type', 'hidden');
            p_input.setAttribute('name', key);
            p_input.setAttribute('value', data[key]);
            mForm.appendChild(p_input);
        }

        return mForm;
    }

});