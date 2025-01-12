import { Component } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { UserService } from '../../services/user.service';
import { RegisterComponent } from '../register/register.component';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [ReactiveFormsModule, RegisterComponent, RouterLink],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {

  loginForm: FormGroup = new FormGroup({
    username: new FormControl('test1'),
    password: new FormControl('test1')
  });

  constructor(private router: Router, public userService: UserService) { }

  login() {
    console.log("Username: " + this.loginForm.value.username + " Password: " + this.loginForm.value.password);
    this.userService.login(this.loginForm.value.username ?? '',
    this.loginForm.value.password ?? '').subscribe(
      {next: (data:any) => {
        console.log(data);
        this.userService.setLoggedUsername(data["username"]);
        this.router.navigate(['/search']);
      },
      error: (error:any) => {
        console.log(error);
      }
      });
  }

  register() {
    this.router.navigate(['/register']);
  }

}
