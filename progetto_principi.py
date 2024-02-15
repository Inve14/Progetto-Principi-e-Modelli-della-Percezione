import random

def simulate_session(num_posts, max_time_per_post):
    total_session_time = 0
    total_posts_viewed = 0
    total_time_on_posts = 0
    
    for _ in range(num_posts):
        post_time = random.uniform(0, max_time_per_post)
        total_time_on_posts += post_time
        total_session_time += post_time
        total_posts_viewed += 1
        
        if random.random() <= 0.7:
            continue
        else:
            break
    
    return total_session_time, total_posts_viewed, total_time_on_posts

def main():
    num_sessions = 1000
    num_posts_per_session = 20
    max_time_per_post = 60

    total_avg_time_on_posts = 0
    total_avg_posts_viewed = 0
    total_session_time = 0

    for _ in range(num_sessions):
        session_time, posts_viewed, time_on_posts = simulate_session(num_posts_per_session, max_time_per_post)
        total_session_time += session_time
        total_avg_time_on_posts += time_on_posts
        total_avg_posts_viewed += posts_viewed

    avg_time_on_posts = total_avg_time_on_posts / num_sessions
    avg_posts_viewed = total_avg_posts_viewed / num_sessions
    avg_session_time = total_session_time / num_sessions

    print("Tempo medio su post: {:.2f} secondi".format(avg_time_on_posts))
    print("Numero medio di post visti: {:.2f}".format(avg_posts_viewed))
    print("Tempo medio di sessione: {:.2f} secondi".format(avg_session_time))

    # Calcolo della concentrazione dell'utente
    total_time_percentage = (total_avg_time_on_posts / total_session_time) * 100

    if total_time_percentage < 20:
        print("La concentrazione è bassa.")
    elif 20 <= total_time_percentage <= 80:
        print("La concentrazione è media.")
    else:
        print("La concentrazione è alta.")
