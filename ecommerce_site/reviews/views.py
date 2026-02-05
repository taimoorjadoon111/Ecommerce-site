from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from store.models import Product
from .models import Review
from .forms import ReviewForm


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    existing_review = Review.objects.filter(
        product=product,
        user=request.user
    ).first()

    if request.method == 'POST':
        if existing_review:
            form = ReviewForm(request.POST, instance=existing_review)
            message = "Your review has been updated successfully!"
        else:
            form = ReviewForm(request.POST)
            message = "Your review has been added successfully!"

        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, message)
            return redirect('store:product_detail', id=product.id)
    else:
        form = ReviewForm(instance=existing_review) if existing_review else ReviewForm()

    return render(request, 'reviews/add_review.html', {
        'product': product,
        'form': form,
        'existing_review': existing_review,
    })


def product_reviews(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)

    total_reviews = reviews.count()
    avg_rating = sum(review.rating for review in reviews) / total_reviews if total_reviews else 0

    return render(request, 'reviews/product_reviews.html', {
        'product': product,
        'reviews': reviews,
        'avg_rating': round(avg_rating, 1),
        'total_reviews': total_reviews,
    })
