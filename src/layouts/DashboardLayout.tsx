import AutoGraphIcon from '@mui/icons-material/AutoGraph';
import CampaignIcon from '@mui/icons-material/Campaign';
import DashboardIcon from '@mui/icons-material/Dashboard';
import GroupsIcon from '@mui/icons-material/Groups';
import InsightsIcon from '@mui/icons-material/Insights';
import MenuIcon from '@mui/icons-material/Menu';
import NotificationsNoneIcon from '@mui/icons-material/NotificationsNone';
import SearchIcon from '@mui/icons-material/Search';
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
import { useTheme } from '@mui/material/styles';
import { useState } from 'react';
import { NavLink, Outlet } from 'react-router-dom';

const drawerWidth = 280;

const navigationItems = [
  { label: 'Dashboard', path: '/dashboard', icon: <DashboardIcon /> },
  { label: 'Campaigns', path: '/campaigns', icon: <CampaignIcon /> },
  { label: 'Audiences', path: '/audiences', icon: <GroupsIcon /> },
  { label: 'Insights', path: '/insights', icon: <InsightsIcon /> },
];

function SidebarContent() {
  return (
    <Stack sx={{ height: '100%' }}>
      <Stack direction="row" spacing={1.5} alignItems="center" sx={{ px: 3, py: 3 }}>
        <Avatar sx={{ bgcolor: 'primary.main' }}>
          <AutoGraphIcon />
        </Avatar>
        <Box>
          <Typography variant="h6" lineHeight={1}>
            GrowthPilot AI
          </Typography>
          <Typography variant="caption" color="text.secondary">
            v0.1.0 growth console
          </Typography>
        </Box>
      </Stack>
      <Divider />
      <List sx={{ px: 2, py: 2 }}>
        {navigationItems.map((item) => (
          <ListItemButton
            key={item.path}
            component={NavLink}
            to={item.path}
            sx={{
              borderRadius: 3,
              mb: 0.75,
              color: 'text.secondary',
              '&.active': {
                bgcolor: 'primary.main',
                color: 'primary.contrastText',
                '& .MuiListItemIcon-root': { color: 'inherit' },
              },
            }}
          >
            <ListItemIcon sx={{ minWidth: 40 }}>{item.icon}</ListItemIcon>
            <ListItemText primary={item.label} primaryTypographyProps={{ fontWeight: 700 }} />
          </ListItemButton>
        ))}
      </List>
      <Box sx={{ flexGrow: 1 }} />
      <Box sx={{ p: 3 }}>
        <Box sx={{ borderRadius: 4, bgcolor: 'primary.light', color: 'primary.contrastText', p: 2.5 }}>
          <Typography fontWeight={800}>AI Growth Brief</Typography>
          <Typography variant="body2" sx={{ mt: 0.75, opacity: 0.9 }}>
            Daily recommendations and anomaly detection are ready for integration.
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
    <Box sx={{ display: 'flex', minHeight: '100vh', bgcolor: 'background.default' }}>
      <AppBar
        position="fixed"
        color="transparent"
        elevation={0}
        sx={{
          width: { lg: `calc(100% - ${drawerWidth}px)` },
          ml: { lg: `${drawerWidth}px` },
          backdropFilter: 'blur(18px)',
          borderBottom: '1px solid',
          borderColor: 'divider',
          bgcolor: 'rgba(246, 248, 251, 0.82)',
        }}
      >
        <Toolbar sx={{ gap: 2 }}>
          {!isDesktop && (
            <IconButton onClick={() => setMobileOpen(true)} edge="start" aria-label="Open navigation">
              <MenuIcon />
            </IconButton>
          )}
          <TextField
            size="small"
            placeholder="Search growth signals..."
            sx={{ maxWidth: 420, flexGrow: 1, display: { xs: 'none', sm: 'block' } }}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <SearchIcon fontSize="small" />
                </InputAdornment>
              ),
            }}
          />
          <Box sx={{ flexGrow: 1 }} />
          <IconButton aria-label="View notifications">
            <NotificationsNoneIcon />
          </IconButton>
          <Avatar alt="Maya Chen" src="https://i.pravatar.cc/120?img=47" />
        </Toolbar>
      </AppBar>

      <Box component="nav" sx={{ width: { lg: drawerWidth }, flexShrink: { lg: 0 } }}>
        <Drawer
          variant="temporary"
          open={mobileOpen}
          onClose={() => setMobileOpen(false)}
          ModalProps={{ keepMounted: true }}
          sx={{ display: { xs: 'block', lg: 'none' }, '& .MuiDrawer-paper': { width: drawerWidth } }}
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

      <Box component="main" sx={{ flexGrow: 1, width: { lg: `calc(100% - ${drawerWidth}px)` }, p: { xs: 2, md: 4 }, pt: { xs: 10, md: 12 } }}>
        <Outlet />
      </Box>
    </Box>
  );
}
