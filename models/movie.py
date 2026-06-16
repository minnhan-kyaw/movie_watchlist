class Movie:
    def __init__(self, id=None, title="", genre="", release_year=None, rating=None, status="", notes=""):
        self.id = id
        self.title = title
        self.genre = genre
        self.release_year = release_year
        self.rating = rating
        self.status = status
        self.year = release_year 
        self.notes = notes if notes and notes.strip() != "" else "This movie have no notes."

    def _validate_rating(self, rating):
        if rating is None: return 0
        try:
            val = int(rating)
            return max(0, min(val, 5))
        except ValueError:
            return 0

    def get_stars_display(self):
        if not self.rating:
            return "No Rating"
        return ""
    
    def get_stars_html(self):
        html = ""
        for i in range(1, 6):
            if i <= self.rating:
                html += '<i class="fa-solid fa-star active-star"></i>'
            else:
                html += '<i class="fa-regular fa-star inactive-star"></i>'
        return html

    def get_status_class(self):
        return f"status-{self.status.lower().replace(' ', '-')}"

    @classmethod
    def from_row(cls, row):
        if not row:
            return None
        data = dict(row)
        return cls(
            id=data.get('id'),
            title=data.get('title'),
            genre=data.get('genre'),
            release_year=data.get('release_year'),
            rating=data.get('rating'),
            status=data.get('status'),
            notes=data.get('notes')
        )

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'genre': self.genre,
            'release_year': self.release_year,
            'year': self.year,
            'rating': self.rating,
            'status': self.status,
            'notes': self.notes
        }

    def getitem(self, item):
        return getattr(self, item)