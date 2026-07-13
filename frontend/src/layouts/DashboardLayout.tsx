import AutoAwesomeIcon from '@mui/icons-material/AutoAwesome';
import DashboardIcon from '@mui/icons-material/Dashboard';
import EditNoteIcon from '@mui/icons-material/EditNote';
import MenuIcon from '@mui/icons-material/Menu';
import RadarIcon from '@mui/icons-material/Radar';
import SearchIcon from '@mui/icons-material/Search';
import TaskAltIcon from '@mui/icons-material/TaskAlt';
import {
  AppBar,
  Avatar,
  Box,
  Divider,
  Drawer,
  IconButton,
  InputAdornment,
  List,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Stack,
  TextField,
  Toolbar,
  Typography,
  useMediaQuery,
} from '@mui/material';
import { alpha, useTheme } from '@mui/material/styles';
import { useState } from 'react';
import { NavLink, Outlet } from 'react-router-dom';

import { designTokens } from '../theme/tokens';

const drawerWidth = 288;

const navigationItems = [
  { label: 'Workspace', path: '/dashboard', icon: <DashboardIcon /> },
  { label: 'Trend Radar', path: '/insights', icon: <RadarIcon /> },
  { label: 'Content Studio', path: '/campaigns', icon: <EditNoteIcon /> },
  { label: 'Action Center', path: '/audiences', icon: <TaskAltIcon /> },
];

function SidebarContent() {
  return (
    <Stack sx={{ height: '100%', bgcolor: 'rgba(255,255,255,0.88)', backdropFilter: 'blur(24px)' }}>
      <Stack direction="row" spacing={1.5} sx={{ alignItems: 'center', px: 3, py: 3 }}>
        <Avatar sx={{ bgcolor: 'primary.main', boxShadow: designTokens.shadows.card }}>
          <AutoAwesomeIcon />
        </Avatar>
        <Box>
          <Typography variant="h6" sx={{ lineHeight: 1 }}>
            GrowthPilot AI
          </Typography>
          <Typography variant="caption" color="text.secondary">
            AI Growth OS v0.3.0
          </Typography>
        </Box>
      </Stack>
      <Divider />
      <List aria-label="Primary navigation" sx={{ px: 2, py: 2 }}>
        {navigationItems.map((item) => (
          <ListItemButton
            key={item.path}
            component={NavLink}
            to={item.path}
            sx={{
              borderRadius: 3,
              mb: 0.75,
              color: 'text.secondary',
              minHeight: 48,
              '&:hover': {
                bgcolor: alpha(designTokens.colors.brandAccent, 0.08),
              },
              '&.active': {
                bgcolor: 'primary.main',
                color: 'primary.contrastText',
                boxShadow: designTokens.shadows.card,
                '& .MuiListItemIcon-root': { color: 'inherit' },
              },
            }}
          >
            <ListItemIcon sx={{ minWidth: 40 }}>{item.icon}</ListItemIcon>
            <ListItemText primary={<Typography sx={{ fontWeight: 800 }}>{item.label}</Typography>} />
          </ListItemButton>
        ))}
      </List>
      <Box sx={{ flexGrow: 1 }} />
      <Box sx={{ p: 3 }}>
        <Box sx={{ borderRadius: 4, bgcolor: 'background.default', border: '1px solid', borderColor: 'divider', p: 2.5 }}>
          <Typography sx={{ fontWeight: 900 }}>Daily operating question</Typography>
          <Typography variant="body2" color="text.secondary" sx={{ mt: 0.75 }}>
            What should I do today to grow?
          </Typography>
        </Box>
      </Box>
    </Stack>
  );
}

export function DashboardLayout() {
  const theme = useTheme();
  const isDesktop = useMediaQuery(theme.breakpoints.up('lg'));
  const [mobileOpen, setMobileOpen] = useState(false);

  const drawer = <SidebarContent />;

  return (
    <Box sx={{ display: 'flex', minHeight: '100vh' }}>
      <AppBar
        position="fixed"
        color="transparent"
        elevation={0}
        sx={{
          width: { lg: `calc(100% - ${drawerWidth}px)` },
          ml: { lg: `${drawerWidth}px` },
          backdropFilter: 'blur(22px)',
          borderBottom: '1px solid',
          borderColor: 'divider',
          bgcolor: 'rgba(248, 250, 252, 0.72)',
        }}
      >
        <Toolbar sx={{ gap: 2, minHeight: { xs: 72, md: 80 } }}>
          {!isDesktop && (
            <IconButton onClick={() => setMobileOpen(true)} edge="start" aria-label="Open navigation">
              <MenuIcon />
            </IconButton>
          )}
          <TextField
            size="small"
            placeholder="Search trends, drafts, tasks..."
            aria-label="Search GrowthPilot workspace"
            sx={{ maxWidth: 460, flexGrow: 1, display: { xs: 'none', sm: 'block' } }}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <SearchIcon fontSize="small" />
                </InputAdornment>
              ),
            }}
          />
          <Box sx={{ flexGrow: 1 }} />
          <Stack direction="row" spacing={1.5} sx={{ alignItems: 'center' }}>
            <Box sx={{ display: { xs: 'none', md: 'block' }, textAlign: 'right' }}>
              <Typography variant="body2" sx={{ fontWeight: 800 }}>
                Maya Chen
              </Typography>
              <Typography variant="caption" color="text.secondary">
                Growth Strategist
              </Typography>
            </Box>
            <Avatar alt="Maya Chen">MC</Avatar>
          </Stack>
        </Toolbar>
      </AppBar>

      <Box component="nav" sx={{ width: { lg: drawerWidth }, flexShrink: { lg: 0 } }}>
        <Drawer
          variant="temporary"
          open={mobileOpen}
          onClose={() => setMobileOpen(false)}
          ModalProps={{ keepMounted: true }}
          sx={{ display: { xs: 'block', lg: 'none' }, '& .MuiDrawer-paper': { width: drawerWidth, border: 0 } }}
        >
          {drawer}
        </Drawer>
        <Drawer
          variant="permanent"
          sx={{ display: { xs: 'none', lg: 'block' }, '& .MuiDrawer-paper': { width: drawerWidth, border: 0 } }}
          open
        >
          {drawer}
        </Drawer>
      </Box>

      <Box component="main" sx={{ flexGrow: 1, width: { lg: `calc(100% - ${drawerWidth}px)` }, px: { xs: 2, sm: 3, md: 4 }, py: { xs: 10, md: 12 } }}>
        <Outlet />
      </Box>
    </Box>
  );
}
