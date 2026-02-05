from django import template

register = template.Library()

@register.filter
def avg_rating(reviews):
    """Calculate average rating from a queryset of reviews"""
    if reviews.exists():
        total = sum(review.rating for review in reviews)
        return round(total / reviews.count(), 1)
    return 0