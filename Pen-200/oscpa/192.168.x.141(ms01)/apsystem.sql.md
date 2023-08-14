-- phpMyAdmin SQL Dump                                                                                                              
-- version 4.7.9 

INSERT INTO `admin` (`id`, `username`, `password`, `firstname`, `lastname`, `photo`, `created_on`) VALUES                                
(1, 'nurhodelta', '$2y$10$fCOiMky4n5hCJx3cpsG20Od4wHtlkCLKmO6VLobJNRIg9ooHTkgjK', 'Neovic', 'Devierte', 'facebook-profile-image.jpeg', '2
018-04-30'); 

INSERT INTO `employees` (`id`, `employee_id`, `firstname`, `lastname`, `address`, `birthdate`, `contact_info`, `gender`, `position_id`, `
schedule_id`, `photo`, `created_on`) VALUES                                                                                              
(1, 'ABC123456789', 'Neovic', 'Devierte', 'Brgy. Mambulac, Silay City', '2018-04-02', '09092735719', 'Male', 1, 2, 'desktop.jpg', '2018-0
4-28'),                                                                                                                                  
(3, 'DYE473869250', 'Julyn', 'Divinagracia', 'E.B. Magalona', '1992-05-02', '09123456789', 'Female', 2, 2, '', '2018-04-30'),            
(4, 'JIE625973480', 'Gemalyn', 'Cepe', 'Carmen, Bohol', '1995-10-02', '09468029840', 'Female', 2, 3, '', '2018-04-30');