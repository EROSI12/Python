def scrape_books():
    for book_div in soup.find_all("div", class_="elementList"):
        title_tag = book_div.find("a", class_="bookTitle")
        author_tag = book_div.find("span", itemprop="name")
        info_tag = book_div.find("span", class_="grayText smallText")

        if title_tag and author_tag:
            title = title_tag.text.strip()
            author = author_tag.text.strip()
            full_link = f"https://www.goodreads.com{title_tag['href']}"
            avg_rating, published = None, None

            if info_tag:
                info_text = info_tag.get_text(strip=True)
                parts = [part.strip() for part in info_text.split("-")]

                for part in parts:
                    if part.startswith("avg rating"):
                        avg_rating = part.split("avg rating")[-1].strip()
                    elif part.startswith("published"):
                        published = part.split("published")[-1].strip()

            genres_response = requests.get(full_link, headers=headers)
            genres_soup = BeautifulSoup(genres_response.text, "html.parser")
            genres = [
                genre.get_text(strip=True)
                for genre in genres_soup.find_all(
                    "span", class_="BookPageMetadataSection__genreButton"
                )
            ]

            books_dict[(title, author)] = {
                "link": full_link,
                "genre": genres,
                "avg_rating": avg_rating,
                "published": published
            }

            if author not in authors:
                authors.append(author)

    return books_dict, authors


print(scrape_books())
