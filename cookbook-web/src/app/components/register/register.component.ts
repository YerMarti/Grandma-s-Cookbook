import { Component } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { UserService } from '../../services/user.service';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [ReactiveFormsModule, RouterLink],
  templateUrl: './register.component.html',
  styleUrl: './register.component.css'
})
export class RegisterComponent {

  registerForm: FormGroup = new FormGroup({
    usernameReg: new FormControl('test1'),
    passwordReg: new FormControl('test1')
  });

  constructor(private router: Router, public userService: UserService) { }

  register() {
    this.userService.register(this.registerForm.value.usernameReg ?? '',
    this.registerForm.value.passwordReg ?? '').subscribe(
      {next: (data:any) => {
        this.userService.setLoggedUsername(data["username"]);
        this.router.navigate(['/search']);
      },
      error: (error:any) => {
        console.log(error);
      }
      });
  }

}
