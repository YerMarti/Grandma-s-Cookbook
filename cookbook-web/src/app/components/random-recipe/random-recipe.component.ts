import { Component, model, ModelSignal } from '@angular/core';
import { KeyValuePipe } from '@angular/common';
import { Recipe } from '../../models/recipe';
import { Subscription } from 'rxjs';
import { RecipeService } from '../../services/recipe.service';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { UserService } from '../../services/user.service';

@Component({
  selector: 'app-random-recipe',
  standalone: true,
  imports: [KeyValuePipe, RouterLink],
  templateUrl: './random-recipe.component.html',
  styleUrl: './random-recipe.component.css'
})
export class RandomRecipeComponent {

  recipe: ModelSignal<Recipe> = model<Recipe>({ id: 0, name: '', category: '', area: '', instructions: '', thumbnail: '', ingredients: {} });
  recipeSubscription!: Subscription;

  constructor(public recipeService: RecipeService, private route: ActivatedRoute, public userService: UserService) { }

  ngOnInit() {
    this.recipeSubscription = this.route.params.subscribe(params => {
      this.recipeService.randomRecipe().subscribe(
        {next: (data:any) => {
          console.log(data);
          this.recipe.set(data);
        }
      });
    });
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

}
