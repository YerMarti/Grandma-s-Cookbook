import { Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { SearchRecipeComponent } from './components/search-recipe/search-recipe.component';
import { FavoritesComponent } from './components/favorites/favorites.component';
import { RandomRecipeComponent } from './components/random-recipe/random-recipe.component';
import { RecipeDetailComponent } from './components/recipe-detail/recipe-detail.component';

export const routes: Routes = [
    {path: 'search', component: SearchRecipeComponent},
    {path: 'favorites', component: FavoritesComponent},
    {path: 'random', component: RandomRecipeComponent},
    {path: 'recipe/:id', component: RecipeDetailComponent},
    {path: '', component: LoginComponent},
];
