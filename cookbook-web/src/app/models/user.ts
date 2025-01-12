import { Recipe } from "./recipe";

export interface User {
    username: string;
    password: string;
    favoriteRecipes: Recipe[];
}