def validate_data(posts):

    valid_posts = []
    rejected_posts = []

    for post in posts:

        reasons = []

        if not isinstance(post.get("userId"), int):
            reasons.append("userId must be an integer")

        if not isinstance(post.get("id"), int):
            reasons.append("id must be an integer")

        if not isinstance(post.get("title"), str) or not post["title"].strip():
            reasons.append("title must be a non-empty string")

        if not isinstance(post.get("body"), str) or not post["body"].strip():
            reasons.append("body must be a non-empty string")

        if reasons:
            rejected_posts.append({
                "record": post,
                "reasons": reasons
            })
        else:
            valid_posts.append(post)

    print("Valid records:", len(valid_posts))
    print("Rejected records:", len(rejected_posts))

    return valid_posts, rejected_posts