from domain.scraping import get_favs, save_recipes


def main():
    print("クラシルからお気に入りレシピ取得")
    recipes = get_favs()
    print("スプレッドシートに保存")
    save_recipes(recipes)


if __name__ == "__main__":
    main()
