import { Component, ModelSignal, model } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { UserService } from '../../services/user.service';
import { Recipe } from '../../models/recipe';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-favorites',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './favorites.component.html',
  styleUrl: './favorites.component.css'
})
export class FavoritesComponent {

  recipes: Recipe[] = [];
  favoritesSubscription!: Subscription;

  constructor(private router: Router, public userService: UserService) { }

  ngOnInit() {
    this.favoritesSubscription = this.userService.getFavoriteRecipes(this.userService.getLoggedUsername()).subscribe({
      next: (data: any) => {
        this.recipes = data;
      },
      error: (err) => {
        console.error(err);
      }
    });
  }

  goToRecipeDetails(recipeId: number) {
    this.router.navigate(['/recipe', recipeId]);
  }

}
