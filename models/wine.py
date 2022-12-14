class Wine():
    wine: dict = {}

    def __init__(self, fixed_acidity:float, volatile_acidity: float, citric_acid: float, residual_sugar: float, chlorides: float, free_sulfur_dioxide: float, total_sulfur_dioxide: float, density: float, pH: float, sulphates: float, alcohol: float, quality: int = None):
        self.wine["fixed acidity"] = fixed_acidity
        self.wine["volatile acidity"] = volatile_acidity
        self.wine["citric acid"] = citric_acid
        self.wine["residual sugar"] = residual_sugar
        self.wine["chlorides"] = chlorides
        self.wine["free sulfur dioxide"] = free_sulfur_dioxide
        self.wine["total sulfur dioxide"] = total_sulfur_dioxide
        self.wine["density"] = density
        self.wine["pH"] = pH
        self.wine["sulphates"] = sulphates
        self.wine["alcohol"] = alcohol
        self.wine["quality"] = quality