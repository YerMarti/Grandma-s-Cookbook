import { Component, ModelSignal, model } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { RecipeService } from '../../services/recipe.service';
import { Recipe } from '../../models/recipe';
import { UserService } from '../../services/user.service';

@Component({
  selector: 'app-search-recipe',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './search-recipe.component.html',
  styleUrl: './search-recipe.component.css'
})
export class SearchRecipeComponent {

  recipes: Recipe[] = [];
  loading: boolean = false;
  error: string | null = null;

  constructor(private router: Router, public recipeService: RecipeService, public userService: UserService) { }

  searchRecipes(name: string) {
    this.loading = true;
    this.error = null;
    this.recipes = [];

    this.recipeService.searchRecipes(name).subscribe({
      next: (data: any) => {
        this.recipes = data;
        this.loading = false;
      },
      error: (err) => {
        this.loading = false;
        this.error = "Error searching recipes.";
        console.error(err);
      }
    });
  }

  goToRecipeDetails(recipeId: number) {
    this.router.navigate(['/recipe', recipeId]);
  }

  addFavorite(recipeId: number) {
    this.userService.addFavoriteRecipe(recipeId.toString()).subscribe({
      next: (data: any) => {
        console.log(data);
      },
      error: (err) => {
        console.error(err);
      }
    });
  }

  randomRecipe() {
    this.router.navigate(['/random']);
  }

}
