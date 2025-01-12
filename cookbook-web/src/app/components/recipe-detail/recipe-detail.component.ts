import { Component, model, ModelSignal } from '@angular/core';
import { KeyValuePipe } from '@angular/common';
import { Recipe } from '../../models/recipe';
import { Subscription } from 'rxjs';
import { RecipeService } from '../../services/recipe.service';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { UserService } from '../../services/user.service';

@Component({
  selector: 'app-recipe-detail',
  standalone: true,
  imports: [KeyValuePipe, RouterLink],
  templateUrl: './recipe-detail.component.html',
  styleUrl: './recipe-detail.component.css'
})
export class RecipeDetailComponent {

  recipe: ModelSignal<Recipe> = model<Recipe>({ id: 0, name: '', category: '', area: '', instructions: '', thumbnail: '', ingredients: {} });
  recipeSubscription!: Subscription;

  constructor(public recipeService: RecipeService, private route: ActivatedRoute, public userService: UserService) { }

  ngOnInit() {
    this.recipeSubscription = this.route.params.subscribe(params => {
      this.recipeService.getRecipe(params['id']).subscribe(
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
