let products = []

function renderProductPreview(product) {
    document.querySelector('div.product-grid-view').innerHTML += [
        `<div class="col-md-4 col-sm-6">`,
            `<div class="product-item">`,
                `<div class="product-img">`,
                    `<a href="single-product-variable.html">`,
                        `<img class="primary-img" src="/static/${product.image}" alt="Product Images">`,
                    `</a>`,
                    `<div class="product-add-action">`,
                        `<ul>`,
                            `<li>`,
                                `<a href="wishlist.html" data-tippy="Add to wishlist" data-tippy-inertia="true"`,
                                   `data-tippy-animation="shift-away" data-tippy-delay="50" data-tippy-arrow="true"`,
                                   `data-tippy-theme="sharpborder">`,
                                    `<i class="pe-7s-like"></i>`,
                                `</a>`,
                            `</li>`,
                            `<li>`,
                                `<a href="cart.html" data-tippy="Add to cart" data-tippy-inertia="true" data-tippy-animation="shift-away" data-tippy-delay="50" data-tippy-arrow="true" data-tippy-theme="sharpborder">`,
                                    `<i class="pe-7s-cart"></i>`,
                                `</a>`,
                            `</li>`,
                        `</ul>`,
                    `</div>`,
                `</div>`,
                `<div class="product-content">`,
                    `<a class="product-name" href="single-product-variable.html">${product.name}</a>`,
                    `<div class="price-box pb-1">`,
                        `<span class="new-price">$ ${product.price}</span>`,
                    `</div>`,
                `</div>`,
            `</div>`,
        `</div>`,
        ].join('\n')
    }

$(document).ready(function () {
    $.ajax(
        {
            url: '/api/product',
            contentType: 'application/json',
            dataType: 'json',
            method: 'get'
        }
    ).done(function (data) {
        document.querySelector('div.product-grid-view').innerHTML = ''
        for (const product of data) {
            renderProductPreview(product)
        }
        products = data
    })
})

$('a.nav-item').click(function (e) {
    e.preventDefault()
    $.ajax(
        {
            url: '/api/product?category_id=' + this.id,
            contentType: 'application/json',
            dataType: 'json',
            method: 'get'
        }
    ).done(function (data) {
        document.querySelector('div.product-grid-view').innerHTML = ''
        for (const product of data) {
            renderProductPreview(product)
        }
        products = data
    })
})

$('form.price-filter').on('submit', function (e) {
    e.preventDefault()
    const minPrice = this.min.value
    const maxPrice = this.max.value
    const data = products.filter(v => v.price >= minPrice && v.price <= maxPrice)
    document.querySelector('div.product-grid-view').innerHTML = ''
    console.log(data)
    if (data.length !== 0) {
        for (const product of data) {
            renderProductPreview(product)
        }
    } else {
        document.querySelector('div.product-grid-view').innerHTML = 'PRODUCT NOT FOUND'
    }
})


$('form#widgets-searchbox').on('submit', function (e) {
    e.preventDefault()
    console.log(this.q.value)
    $.ajax(
        {
            url: '/api/product?q=' + this.q.value,
            contentType: 'application/json',
            dataType: 'json',
            method: 'get'
        }
    ).done(function (data) {
        document.querySelector('div.product-grid-view').innerHTML = ''
        for (const product of data) {
            renderProductPreview(product)
        }
        products = data
    })
})